"""Short learning file for regex, JSON, and CSV parsing.

Run:
    python3 T20_V/python/15_regex_json_csv_learning.py
"""

from __future__ import annotations

import csv
import json
from pathlib import Path
import re
import w_r


BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"


def detect_failures(log_path: Path) -> list[str]:
    failure_pattern = re.compile(r"(ERROR|Kernel panic|watchdog reset)")
    failures: list[str] = []
    for line in log_path.read_text(encoding="utf-8").splitlines():
        if failure_pattern.search(line):
            failures.append(line)
    return failures


def read_json_summary(json_path: Path) -> dict[str, object]:
    return json.loads(json_path.read_text(encoding="utf-8"))


def read_csv_results(csv_path: Path) -> list[dict[str, str]]:
    with csv_path.open(encoding="utf-8", newline="") as file_handle:
        return list(csv.DictReader(file_handle))

@w_r
def main() -> int:
    failures = detect_failures(DATA_DIR / "sample_device.log")
    summary = read_json_summary(DATA_DIR / "sample_report.json")
    csv_rows = read_csv_results(DATA_DIR / "sample_results.csv")

    print(f"failure lines: {len(failures)}")
    for line in failures:
        print(f"- {line}")

    print(f"json summary status: {summary['status']}")
    print(f"csv cases loaded: {len(csv_rows)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())