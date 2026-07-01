"""Short learning file for SSH-style device commands.

Run:
    python3 T20_V/python/07_paramiko_ssh_learning.py

Optional:
    pip install paramiko
"""

from __future__ import annotations

from dataclasses import dataclass
import w_r

try:
    import paramiko
except ImportError:  # pragma: no cover - learning fallback for missing dependency.
    paramiko = None


@dataclass
class FakeSSHClient:
    def exec_command(self, command: str) -> tuple[None, list[str], list[str]]:
        print(f"ssh exec: {command}")
        if command == "systemctl is-active app":
            return None, ["active\n"], []
        if command == "cat /etc/os-release | head -n 1":
            return None, ["NAME=EmbeddedLinux\n"], []
        return None, [], ["unknown command\n"]


def run_remote_check(ssh_client: FakeSSHClient, command: str, expected_text: str) -> bool:
    _, stdout_lines, stderr_lines = ssh_client.exec_command(command)
    output = "".join(stdout_lines + stderr_lines).strip()
    print(f"output: {output}")
    return expected_text in output

@w_r
def main() -> int:
    ssh_client = FakeSSHClient()
    app_ok = run_remote_check(ssh_client, "systemctl is-active app", "active")
    os_ok = run_remote_check(ssh_client, "cat /etc/os-release | head -n 1", "EmbeddedLinux")

    if not app_ok or not os_ok:
        print("FAIL: remote SSH checks did not match expected output")
        return 1

    print("PASS: remote SSH checks matched expected output")
    if paramiko is None:
        print("Note: paramiko is not installed, so this run used a fake SSH client for learning.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())