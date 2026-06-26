#!/usr/bin/env bash

set -euo pipefail

target_host="${1:-127.0.0.1}"

check_ping() {
    local host="$1"

    # A tiny smoke check should be fast and return a clear signal.
    if ping -c 1 "$host" >/dev/null 2>&1; then
        echo "[PASS] ping to ${host}"
    else
        echo "[FAIL] ping to ${host}"
        return 1
    fi
}

check_python() {
    if python3 --version >/dev/null 2>&1; then
        echo "[PASS] python3 available"
    else
        echo "[FAIL] python3 missing"
        return 1
    fi
}

main() {
    echo "Running tiny device smoke runner"
    check_ping "$target_host"
    check_python
    echo "Smoke runner completed"
}

main