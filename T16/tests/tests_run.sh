#!/bin/bash

# Step 1: Enable strict mode.
# -e: stop on first failing command
# -u: fail on unset variables
# -o pipefail: fail pipeline if any command fails
set -euo pipefail

# Step 2: Resolve script location.
# BASH_SOURCE points to this script file.
BFS=$BASH_SOURCE
SR=$(dirname "$BFS")

# Step 3: Compute repository root (two levels above tests/).
REPO_ROOT=$(cd "$SR/../.." && pwd)
echo "$REPO_ROOT"

# Step 4: Move to T16 directory (parent of tests/) to keep relative paths stable.
cd "$SR/../"
echo "pwd | $(pwd)"
SR2="$(pwd)"
echo "$SR2"

# Step 5: Start the FastAPI app in the background so the script can continue.
bash $SR2/app_run.sh &

# Step 6: Save PID of the background process for cleanup.
APP_PID=$!

# Step 7: Define cleanup logic.
# This runs on script exit and stops the background app process.
cleanup() {
	# kill -0 is a safe existence check for the process.
	if kill -0 "$APP_PID" 2>/dev/null; then
		# Send termination signal.
		kill "$APP_PID"
		# Wait for process exit; ignore non-critical wait errors during teardown.
		wait "$APP_PID" 2>/dev/null || true
	fi
}

# Step 8: Register cleanup for normal exit, errors, and interruptions.
trap cleanup EXIT

# Step 9: Give uvicorn time to bind to the port before tests start.
sleep 2

# Step 10: Activate virtualenv so pytest uses project dependencies.
if [[ -f "$REPO_ROOT/.venv/bin/activate" ]]; then
	source "$REPO_ROOT/.venv/bin/activate"
else
	echo "Missing virtualenv activation script: $REPO_ROOT/.venv/bin/activate"
	exit 1
fi

# Step 11: Run only tests marked with "easy".
pytest -vv -rP -s -m easy