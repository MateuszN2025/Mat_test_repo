#!/bin/bash

set -Eeuo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
echo ---------------------
echo SCRIPT_DIR = $SCRIPT_DIR


PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
echo ---------------------
echo PROJECT_ROOT = $PROJECT_ROOT


WORKSPACE_DIR="${WORKSPACE:-/home/mniedziolka/jenkins-agent/workspace/at_1}"
echo ---------------------
echo WORKSPACE_DIR = $WORKSPACE_DIR

# ${VAR:-x}	use x if VAR unset or empty (no assignment)
# ${VAR-x}	use x only if VAR unset (empty stays empty)
# ${VAR:=x}	same as :- but also assigns x to VAR
# ${VAR:?msg}	error out with msg if unset/empty
# ${VAR:+x}	use x if VAR is set & non-empty, else empty
# It's the standard idiom for "configurable with a default."

ALLURE_RESULTS_DIR="${ALLURE_RESULTS_DIR:-$WORKSPACE_DIR/allure-results}"
echo ---------------------
echo ALLURE_RESULTS_DIR = $ALLURE_RESULTS_DIR


PYTHON_BIN="${PYTHON_BIN:-python3}"
echo ---------------------
echo PYTHON_BIN = $PYTHON_BIN
echo ---------------------

rm -rf "$ALLURE_RESULTS_DIR"
mkdir -p "$ALLURE_RESULTS_DIR"

# cd "$PROJECT_ROOT" # T11/
# from .helpers import execute_command ✅
# from helpers import execute_command  ❌


cd "$SCRIPT_DIR" # T11/tests/
# from helpers import execute_command  ✅
# from .helpers import execute_command ✅

source "$SCRIPT_DIR/.env.sh"
# "$PYTHON_BIN" -m pytest --alluredir="$ALLURE_RESULTS_DIR" -vv -rP -s
"$PYTHON_BIN" -m pytest --alluredir="$ALLURE_RESULTS_DIR" -vv -rP -s -k "div or mul"
# "$PYTHON_BIN" -m pytest --alluredir="$ALLURE_RESULTS_DIR" -vv -rP -s -m optimal pytest 