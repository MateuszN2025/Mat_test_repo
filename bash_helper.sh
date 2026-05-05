#!/usr/bin/env bash

# Fail fast on common shell problems:
# -e: stop on the first failing command
# -E: preserve trap behavior in functions/subshells
# -u: treat unset variables as errors
# -o pipefail: fail a pipeline if any command in it fails
set -Eeuo pipefail

# Resolve the absolute directory of this helper script.
# This makes the wrapper independent from the caller's current working directory,
# so the repository always dispatches to the same pinned test runner.
SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"

# Replace the current shell process with the real test entrypoint.
# Using exec avoids leaving this tiny wrapper process running and guarantees
# that exit codes come directly from the underlying test script.
exec bash "$SCRIPT_DIR/T11/tests/run_test.sh"