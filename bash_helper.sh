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
# ################################################################
# SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
# ################################################################
#!/usr/bin/env bash

SCRIPT_PATH="${BASH_SOURCE[0]}"
echo "1. script path     = $SCRIPT_PATH"

SCRIPT_PARENT="$(dirname -- "$SCRIPT_PATH")"
echo "2. parent folder   = $SCRIPT_PARENT"

cd -- "$SCRIPT_PARENT"
echo "3. after cd, here  = $(pwd)"

SCRIPT_DIR="$(pwd)"
echo "4. final SCRIPT_DIR= $SCRIPT_DIR"

# 1
# ${BASH_SOURCE[0]}
#   /home/mniedziolka/PP/Mat_test_repo/bash_helper.sh
# 2
# dirname "${BASH_SOURCE[0]}" <-- dirname removes the file name and leaves only the folder.
#   /home/mniedziolka/PP/Mat_test_repo
# 3
# cd -- "$(dirname -- "${BASH_SOURCE[0]}")"
#   The shell changes directory into:
#       /home/mniedziolka/PP/Mat_test_repo
#           cd "/home/mniedziolka/PP/Mat_test_repo" <-- LOCAL
#           cd "/home/mniedziolka/jenkins-agent/workspace/at_1/" <-- JENKINS
# 4
# pwd
#   /home/mniedziolka/PP/Mat_test_repo
# 5
# $(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)
#   $(...)
#       So now Bash captures the text from pwd
# 6
# SCRIPT_DIR=/home/mniedziolka/PP/Mat_test_repo

# Replace the current shell process with the real test entrypoint.
# Using exec avoids leaving this tiny wrapper process running and guarantees
# that exit codes come directly from the underlying test script.
exec bash "$SCRIPT_DIR/T11/tests/run_test.sh"
# 1
# "$SCRIPT_DIR/T11/tests/run_test.sh"
#   /home/mniedziolka/PP/Mat_test_repo   /T11/tests/run_test.sh
# 2
# bash "/home/mniedziolka/PP/Mat_test_repo/T11/tests/run_test.sh"
# 3
# exec bash "/home/mniedziolka/PP/Mat_test_repo/T11/tests/run_test.sh"
#   without exec: script A starts script B
#       Without exec
#           bash_helper.sh -> run_test.sh -> back to bash_helper.sh -> exit
#   with exec: script A turns into script B ❗
#       With exec:
#           bash_helper.sh -> becomes run_test.sh