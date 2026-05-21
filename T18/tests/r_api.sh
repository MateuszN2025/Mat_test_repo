#!/bin/bash

# $( ... ) means command substitution
# It runs commands and captures their output as text.

# ${ ... } means parameter expansion
# It expands a variable (or transforms it), but it does not run shell commands.

# What matters:
# $( ... ) runs shell commands and captures stdout as text.
# $(( ... )) evaluates an arithmetic expression and returns a number.
# ${ ... } expands or transforms variable values.

# echo "-> $ds"
# echo "-> $pf"
# echo "-> $rd"
# echo "-> $af"

bs=${BASH_SOURCE}
ds=$(dirname "$bs")
pf="$(cd "$ds/.." && pwd)"
rd="$(cd "$ds/../.." && pwd)"
af="$(cd "$rd/T18/api" && pwd)"
source "$rd/.venv/bin/activate"
cd "$af"
uvicorn api_2:api_2 --reload --host "${APP_HOST:-127.0.0.1}" --port "${APP_PORT:-8000}"
