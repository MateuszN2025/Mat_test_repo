# Linux and Bash for QA Automation

## What matters

Linux fluency saves time during debugging, CI work, and remote device investigation.

## Commands worth knowing well

- `ps`, `pgrep`, `top`: inspect processes
- `ss`, `netstat`, `lsof`: inspect ports and connections
- `journalctl`, `dmesg`, `tail -f`: inspect logs
- `grep`, `awk`, `sed`, `cut`, `sort`, `uniq`: filter output
- `find`, `xargs`: locate and process files
- `chmod`, `chown`: fix permission issues
- `curl`, `ping`: basic reachability checks

## Bash habits that matter

- Use `set -euo pipefail` in automation scripts
- Quote variables: `"$var"`
- Prefer functions for repeated actions
- Fail fast with clear error messages
- Print enough context for CI logs

## Typical QA use cases

- Check if a device is reachable
- Parse logs after a failed deployment
- Start a service and verify it stayed up
- Collect artifacts from test machines

## Senior-level insight

The best Bash in CI is usually short, explicit, and disposable. If a script grows complex, move the logic into Python and keep Bash as the thin entry layer.

## Practice task

Write a small script that checks a PID file, verifies the process exists, and prints a helpful error if it does not.