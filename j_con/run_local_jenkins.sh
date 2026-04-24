#!/usr/bin/env bash

set -Eeuo pipefail

readonly SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
readonly ENV_FILE="$SCRIPT_DIR/.env"
readonly IMAGE_NAME="local/jenkins-automation-pass:lts"
readonly CONTAINER_NAME="jenkins-local-pass"
readonly VOLUME_NAME="jenkins_home_local_pass"
readonly INIT_DIR="$SCRIPT_DIR/init.groovy.d"
readonly AGENT_DIR="$(cd "$SCRIPT_DIR/../j_ag" && pwd)"
readonly AGENT_SCRIPT="$AGENT_DIR/run_jenkins_agent.sh"
readonly AGENT_PID_FILE="$AGENT_DIR/run_jenkins_agent.pid"
readonly AGENT_LOG_FILE="$AGENT_DIR/run_jenkins_agent.log"

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
	: "${JENKINS_URL:=http://172.28.221.58:${JENKINS_HTTP_PORT}/}"
}

container_exists() {
	podman container exists "$CONTAINER_NAME"
}

agent_is_running() {
	if [[ ! -f "$AGENT_PID_FILE" ]]; then
		return 1
	fi

	local agent_pid
	agent_pid="$(<"$AGENT_PID_FILE")"
	if [[ -z "$agent_pid" ]]; then
		rm -f "$AGENT_PID_FILE"
		return 1
	fi

	if kill -0 "$agent_pid" 2>/dev/null; then
		return 0
	fi

	rm -f "$AGENT_PID_FILE"
	return 1
}

build_image() {
	podman build -t "$IMAGE_NAME" "$SCRIPT_DIR"
}

wait_for_jenkins() {
	local attempt
	for attempt in $(seq 1 60); do
		if curl -fsS "$JENKINS_URL/login" >/dev/null 2>&1; then
			return 0
		fi
		sleep 2
	done

	echo "Timed out waiting for Jenkins at $JENKINS_URL"
	return 1
}

start_agent_background() {
	if [[ ! -x "$AGENT_SCRIPT" ]]; then
		echo "Skipping agent autostart: missing executable $AGENT_SCRIPT"
		return 0
	fi

	if [[ ! -f "$AGENT_DIR/.env" ]]; then
		echo "Skipping agent autostart: missing $AGENT_DIR/.env"
		return 0
	fi

	if agent_is_running; then
		echo "Jenkins agent is already running in the background."
		return 0
	fi

	require_command curl
	(
		set -Eeuo pipefail
		wait_for_jenkins
		cd "$AGENT_DIR"
		exec "$AGENT_SCRIPT" run >> "$AGENT_LOG_FILE" 2>&1
	) &
	echo "$!" > "$AGENT_PID_FILE"
	echo "Started Jenkins agent launcher in background. pid=$(<"$AGENT_PID_FILE")"
	echo "Agent log: $AGENT_LOG_FILE"
}

stop_agent_background() {
	if ! agent_is_running; then
		return 0
	fi

	local agent_pid
	agent_pid="$(<"$AGENT_PID_FILE")"
	kill "$agent_pid" 2>/dev/null || true
	rm -f "$AGENT_PID_FILE"
	echo "Stopped Jenkins agent background process."
}

require_command() {
	if ! command -v "$1" >/dev/null 2>&1; then
		echo "Missing required command: $1"
		exit 1
	fi
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

	start_agent_background

	echo "Jenkins is starting at $JENKINS_URL"
	echo "Login with username '$JENKINS_ADMIN_ID' and the password from $ENV_FILE"
}

down() {
	stop_agent_background
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
	echo "Jenkins state reset. Run './run_local_jenkins.sh up' to start fresh."
}

status() {
	podman ps -a --filter "name=$CONTAINER_NAME"
	podman volume ls --filter "name=$VOLUME_NAME"
	if agent_is_running; then
		echo "Agent background process: running (pid $(<"$AGENT_PID_FILE"))"
	else
		echo "Agent background process: stopped"
	fi
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
		echo "Usage: ./run_local_jenkins.sh {up|down|logs|reset|status}"
		exit 1
		;;
esac