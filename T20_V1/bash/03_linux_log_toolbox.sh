#!/usr/bin/env bash

set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
log_file="${repo_root}/T20_V/data/sample_device.log"

echo "=== grep: failure lines ==="
grep -nE 'ERROR|Kernel panic|watchdog reset' "${log_file}" || true

echo
echo "=== awk: count levels ==="
awk '{count[$1]++} END {for (level in count) print level, count[level]}' "${log_file}"

echo
echo "=== sed: show service lines without prefix ==="
sed -n 's/^INFO service=//p' "${log_file}"

echo
echo "=== tail: latest lines ==="
tail -n 3 "${log_file}"

echo
echo "=== find: sample data files ==="
find "${repo_root}/T20_V/data" -maxdepth 1 -type f | sort

echo
echo "Interview note: on a real device, replace this sample file with /var/log output or journalctl dumps."