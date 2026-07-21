#!/usr/bin/env bash

set -euo pipefail

echo "=== localhost reachability ==="
ping -c 1 127.0.0.1

echo
echo "=== network interfaces ==="
if command -v ip >/dev/null 2>&1; then
    ip -brief a
elif command -v ifconfig >/dev/null 2>&1; then
    ifconfig
else
    echo "Neither ip nor ifconfig is available"
fi

echo
echo "=== listening tcp ports ==="
if command -v ss >/dev/null 2>&1; then
    ss -ltn
elif command -v netstat >/dev/null 2>&1; then
    netstat -ltn
else
    echo "Neither ss nor netstat is available"
fi

echo
echo "=== /dev examples ==="
find /dev -maxdepth 1 \( -name 'tty*' -o -name 'video*' \) | head -n 10 || true

echo
echo "Interview note: /dev/ttyUSB0 is typically where Linux exposes a USB serial adapter."