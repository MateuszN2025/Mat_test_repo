"""Short learning file for subprocess usage in QA automation.

Run:
    python3 T20_V/python/01_subprocess_learning.py
"""

from __future__ import annotations

import shlex
import subprocess


def run_command(command: str) -> subprocess.CompletedProcess[str]:
    """Run a shell-like command safely and capture output.

    Important: shlex.split keeps the example close to terminal usage,
    but still avoids shell=True for better safety and predictability.
    """
    return subprocess.run(
        shlex.split(command),
        text=True,
        capture_output=True,
        check=False,
        timeout=5,
    )


def print_result(title: str, result: subprocess.CompletedProcess[str]) -> None:
    # Return code is the first thing to inspect in CI or device checks.
    print(f"\n=== {title} ===")
    print(f"return code: {result.returncode}")
    print(f"stdout: {result.stdout.strip() or '<empty>'}")
    print(f"stderr: {result.stderr.strip() or '<empty>'}")


if __name__ == "__main__":
    print("Subprocess learning example for QA automation")

    hostname_result = run_command("hostname")
    print_result("hostname", hostname_result)

    # This style is common in smoke tests: run command, inspect code, log output.
    python_result = run_command("python3 --version")
    print_result("python version", python_result)

    if python_result.returncode != 0:
        print("Important: a non-zero return code should fail the test or pipeline stage.")