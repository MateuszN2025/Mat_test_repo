#!/usr/bin/env bash

set -euo pipefail
echo "➖➖➖➖➖➖➖➖"
# $BASH_SOURCE is a bash array 
# (used here as a string) that contains the path to the script being executed.

echo "BASH_SOURCE $BASH_SOURCE"
BASH_FILE_SOURCE=$BASH_SOURCE
echo "BASH_FILE_SOURCE $BASH_FILE_SOURCE"

# When you run bash app_run.sh from inside T16, 
# $BASH_SOURCE is just app_run.sh (no directory part),
# so dirname app_run.sh returns . (current directory).
# SCRIPT_DIR=$(dirname $BASH_FILE_SOURCE)

# dirname alone returns "." when script is called without a path prefix.
# cd + pwd resolves the absolute directory regardless of how the script was called.
SCRIPT_DIR="$(cd "$(dirname "$BASH_FILE_SOURCE")" && pwd)"

echo "SCRIPT_DIR $SCRIPT_DIR"
cd "$SCRIPT_DIR/.."

REPO_ROOT=$(pwd)
echo "REPO_ROOT $REPO_ROOT"
echo "-----------"


# SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

if [[ ! -f "$REPO_ROOT/.venv/bin/activate" ]]; then
	echo "Missing virtualenv activation script: $REPO_ROOT/.venv/bin/activate"
	exit 1
fi

source "$REPO_ROOT/.venv/bin/activate"

cd "$SCRIPT_DIR/app"
exec uvicorn app1:app1 --reload --host 127.0.0.1 --port 8000

echo "➖➖➖➖➖➖➖➖"