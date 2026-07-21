#!/usr/bin/env bash

set -euo pipefail

temp_script="/tmp/t20_v_permissions_demo.sh"

echo "=== current shell process ==="
ps -p $$ -o pid,ppid,comm,%cpu,%mem

echo
echo "=== background process demo ==="
sleep 30 &
sleep_pid="$!"
ps -p "${sleep_pid}" -o pid,comm,etime
kill "${sleep_pid}"
wait "${sleep_pid}" || true
echo "killed background pid ${sleep_pid}"

echo
echo "=== chmod and exit codes ==="
cat > "${temp_script}" <<'EOF'
#!/usr/bin/env bash
echo "demo script ran"
exit 0
EOF

chmod +x "${temp_script}"
"${temp_script}"
echo "exit code was $?"

echo
echo "=== environment variable demo ==="
export DEVICE_HOST="127.0.0.1"
echo "DEVICE_HOST=${DEVICE_HOST}"

echo
echo "Interview note: CI failures often come from missing execute permissions or the wrong environment variable."