"""Short learning file that simulates a tiny embedded smoke check.

Run:
    python3 T20_V/python/02_embedded_smoke_check.py
"""

from __future__ import annotations

import shlex
import subprocess
from dataclasses import dataclass
import w_r


@dataclass
class CheckResult:
    name: str
    passed: bool
    details: str


def run_check(name: str, command: str) -> CheckResult:
    try:
        # timeout prevents a hanging device check from blocking the whole suite.
        result = subprocess.run(
            shlex.split(command),
            text=True,
            capture_output=True,
            check=False,
            timeout=3,
        )
    except subprocess.TimeoutExpired:
        return CheckResult(name=name, passed=False, details="command timed out")

    passed = result.returncode == 0
    details = result.stdout.strip() or result.stderr.strip() or "no output"
    return CheckResult(name=name, passed=passed, details=details)

@w_r
def main() -> int:
    checks = [
        # In a real lab, replace these with health endpoints, service checks, or device CLI commands.
        run_check("device reachable", "ping -c 1 127.0.0.1"),
        run_check("python available", "python3 --version"),
    ]

    failed = False
    for check in checks:
        status = "PASS" if check.passed else "FAIL"
        print(f"[{status}] {check.name}: {check.details}")
        if not check.passed:
            failed = True

    # CI systems usually rely on the final process exit code.
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())