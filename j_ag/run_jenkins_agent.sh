#!/usr/bin/env bash

set -Eeuo pipefail

readonly SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
readonly ENV_FILE="$SCRIPT_DIR/.env"
readonly AGENT_JAR="$SCRIPT_DIR/agent.jar"
readonly WORK_DIR="$SCRIPT_DIR/remoting"
readonly LOG_DIR="$SCRIPT_DIR/logs"

load_env() {
	if [[ ! -f "$ENV_FILE" ]]; then
		cp "$SCRIPT_DIR/.env.example" "$ENV_FILE"
		echo "Created $ENV_FILE from .env.example. Fill in AGENT_SECRET before continuing."
		return 1
	fi

	set -a
	# shellcheck disable=SC1090
	. "$ENV_FILE"
	set +a

	: "${JENKINS_URL:=http://127.0.0.1:8080/}"
	: "${AGENT_NAME:=local-agent}"
	: "${AGENT_SECRET:=replace-with-agent-secret}"
	: "${AGENT_WEB_SOCKET:=true}"
	: "${AGENT_TUNNEL:=}"
	: "${JAVA_BIN:=java}"
	readonly AGENT_JAR_URL="${JENKINS_URL%/}/jnlpJars/agent.jar"
}

require_command() {
	if ! command -v "$1" >/dev/null 2>&1; then
		echo "Missing required command: $1"
		exit 1
	fi
}

download_jar() {
	load_env || exit 1
	require_command curl
	mkdir -p "$LOG_DIR"
	curl -fsSL "$AGENT_JAR_URL" -o "$AGENT_JAR"
	echo "Downloaded agent jar to $AGENT_JAR"
}

run_agent() {
	load_env || exit 1
	require_command "$JAVA_BIN"
	[[ -f "$AGENT_JAR" ]] || download_jar
	mkdir -p "$WORK_DIR" "$LOG_DIR"

	local -a cmd
	cmd=(
		"$JAVA_BIN"
		-jar "$AGENT_JAR"
		-url "$JENKINS_URL"
		-secret "$AGENT_SECRET"
		-name "$AGENT_NAME"
		-workDir "$WORK_DIR"
	)

	if [[ "$AGENT_WEB_SOCKET" == "true" ]]; then
		cmd+=( -webSocket )
	fi

	if [[ -n "$AGENT_TUNNEL" ]]; then
		cmd+=( -tunnel "$AGENT_TUNNEL" )
	fi

	echo "Starting Jenkins agent '$AGENT_NAME' against $JENKINS_URL"
	"${cmd[@]}"
}

status() {
	load_env || exit 1
	echo "JENKINS_URL=$JENKINS_URL"
	echo "AGENT_NAME=$AGENT_NAME"
	echo "AGENT_JAR=$AGENT_JAR"
	echo "WORK_DIR=$WORK_DIR"
	if [[ -f "$AGENT_JAR" ]]; then
		echo "agent.jar: present"
	else
		echo "agent.jar: missing"
	fi
	if [[ -d "$WORK_DIR" ]]; then
		echo "work dir: present"
	else
		echo "work dir: missing"
	fi
}

clean() {
	rm -rf "$WORK_DIR" "$LOG_DIR"
	echo "Removed local runtime directories. agent.jar was kept."
}

reset() {
	clean
	rm -f "$AGENT_JAR"
	echo "Removed local runtime directories and agent.jar."
}

case "${1:-}" in
	download-jar)
		download_jar
		;;
	run)
		run_agent
		;;
	status)
		status
		;;
	clean)
		clean
		;;
	reset)
		reset
		;;
	*)
		echo "Usage: ./run_jenkins_agent.sh {download-jar|run|status|clean|reset}"
		exit 1
		;;
	esac
