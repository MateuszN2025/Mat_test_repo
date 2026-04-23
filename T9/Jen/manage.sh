#!/usr/bin/env bash

set -Eeuo pipefail

readonly SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
readonly ENV_FILE="$SCRIPT_DIR/.env"
readonly IMAGE_NAME="local/jenkins-automation:lts"
readonly CONTAINER_NAME="jenkins-local"
readonly VOLUME_NAME="jenkins_home_local"
readonly INIT_DIR="$SCRIPT_DIR/init.groovy.d"

load_env() {
	if [[ ! -f "$ENV_FILE" ]]; then
		cp "$SCRIPT_DIR/.env.example" "$ENV_FILE"
		echo "Created $ENV_FILE from .env.example. Review the admin password before continuing."
		return 1
	fi

	set -a
	# shellcheck disable=SC1090
	. "$ENV_FILE"
	set +a

	: "${JENKINS_HTTP_PORT:=8080}"
	: "${JENKINS_AGENT_PORT:=50000}"
	: "${JENKINS_ADMIN_ID:=admin}"
	: "${JENKINS_ADMIN_PASSWORD:=admin-local-change-me}"
	: "${JENKINS_ADMIN_EMAIL:=admin@example.test}"
	: "${JENKINS_URL:=http://127.0.0.1:${JENKINS_HTTP_PORT}/}"
}

container_exists() {
	podman container exists "$CONTAINER_NAME"
}

build_image() {
	podman build -t "$IMAGE_NAME" "$SCRIPT_DIR"
}

write_init_script() {
	mkdir -p "$INIT_DIR"
	cat > "$INIT_DIR/01-admin-user.groovy" <<'EOF'
import hudson.security.HudsonPrivateSecurityRealm
import jenkins.model.Jenkins

def instance = Jenkins.get()
def adminId = System.getenv('JENKINS_ADMIN_ID')
def adminPassword = System.getenv('JENKINS_ADMIN_PASSWORD')

if (!adminId || !adminPassword) {
	println('Skipping admin bootstrap: missing JENKINS_ADMIN_ID or JENKINS_ADMIN_PASSWORD')
	return
}

def realm = instance.getSecurityRealm()
if (!(realm instanceof HudsonPrivateSecurityRealm)) {
	println('Skipping admin bootstrap: security realm is not HudsonPrivateSecurityRealm')
	return
}

def existingUser = realm.getUser(adminId)
if (existingUser == null) {
	realm.createAccount(adminId, adminPassword)
	println("Created Jenkins admin user '${adminId}' from environment")
} else {
	def details = existingUser.getProperty(HudsonPrivateSecurityRealm.Details)
	if (details == null || !details.isPasswordCorrect(adminPassword)) {
		def fromPlainPassword = HudsonPrivateSecurityRealm.Details.class.getDeclaredMethod('fromPlainPassword', String)
		fromPlainPassword.setAccessible(true)
		existingUser.addProperty(fromPlainPassword.invoke(null, adminPassword))
		existingUser.save()
		println("Updated Jenkins admin password for '${adminId}' from environment")
	}
}
EOF
}

ensure_port_available() {
	local conflicting
	conflicting="$(podman ps --format '{{.Names}} {{.Ports}}' | grep -E ":${JENKINS_HTTP_PORT}->|:${JENKINS_AGENT_PORT}->" | grep -v "^${CONTAINER_NAME} " || true)"

	if [[ -n "$conflicting" ]]; then
		echo "Port conflict detected. Stop the existing container first or change ports in .env."
		echo "$conflicting"
		exit 1
	fi
}

up() {
	load_env || exit 1
	ensure_port_available
	write_init_script
	build_image

	if container_exists; then
		podman rm -f "$CONTAINER_NAME" >/dev/null
	fi

	podman volume exists "$VOLUME_NAME" || podman volume create "$VOLUME_NAME" >/dev/null

	podman run -d \
		--name "$CONTAINER_NAME" \
		--restart unless-stopped \
		-p "$JENKINS_HTTP_PORT:8080" \
		-p "$JENKINS_AGENT_PORT:50000" \
		-e CASC_JENKINS_CONFIG=/usr/share/jenkins/ref/casc_configs/jenkins.yaml \
		-e JAVA_OPTS=-Djenkins.install.runSetupWizard=false \
		-e JENKINS_ADMIN_ID="$JENKINS_ADMIN_ID" \
		-e JENKINS_ADMIN_PASSWORD="$JENKINS_ADMIN_PASSWORD" \
		-e JENKINS_ADMIN_EMAIL="$JENKINS_ADMIN_EMAIL" \
		-e JENKINS_URL="$JENKINS_URL" \
		-v "$VOLUME_NAME:/var/jenkins_home:Z" \
		-v "$INIT_DIR:/var/jenkins_home/init.groovy.d:Z" \
		"$IMAGE_NAME"

	echo "Jenkins is starting at $JENKINS_URL"
	echo "Jenkins runs without a login page in this local-only setup."
}

down() {
	if container_exists; then
		podman rm -f "$CONTAINER_NAME"
	fi
}

logs() {
	podman logs -f "$CONTAINER_NAME"
}

reset() {
	down || true
	if podman volume exists "$VOLUME_NAME"; then
		podman volume rm "$VOLUME_NAME"
	fi
	echo "Jenkins state reset. Run './manage.sh up' to start fresh."
}

status() {
	podman ps -a --filter "name=$CONTAINER_NAME"
	podman volume ls --filter "name=$VOLUME_NAME"
}

case "${1:-}" in
	up)
		up
		;;
	down)
		down
		;;
	logs)
		logs
		;;
	reset)
		reset
		;;
	status)
		status
		;;
	*)
		echo "Usage: ./manage.sh {up|down|logs|reset|status}"
		exit 1
		;;
esac