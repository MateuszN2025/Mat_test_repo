#!/usr/bin/env bash

# Strict mode makes failures visible early, which is critical in CI and lab scripts.
set -euo pipefail

print_section() {
    local title="$1"
    echo
    echo "=== ${title} ==="
}

print_section "bash strict mode learning"

# Quoting variables prevents word-splitting bugs.
current_user="${USER:-unknown}"
echo "Current user: ${current_user}"

# command -v is a safe way to check if a tool exists.
if command -v python3 >/dev/null 2>&1; then
    echo "python3 is available"
else
    echo "python3 is missing"
    exit 1
fi

print_section "done"
echo "This script demonstrates safe defaults for automation shell scripts."