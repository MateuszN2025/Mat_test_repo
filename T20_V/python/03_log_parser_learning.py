"""Short learning file for simple log parsing.

Run:
    python3 T20_V/python/03_log_parser_learning.py
"""

from __future__ import annotations

from collections import Counter
import w_r


LOG_LINES = [
    "INFO device boot completed",
    "INFO network connected",
    "WARNING signal weak",
    "ERROR camera stream not started",
    "INFO retry scheduled",
]


def parse_levels(lines: list[str]) -> Counter[str]:
    counts: Counter[str] = Counter()
    for line in lines:
        # Splitting by the first token is a simple but common log summary technique.
        level = line.split()[0]
        counts[level] += 1
    return counts

@w_r
def main():
    counts = parse_levels(LOG_LINES)
    print("Log level summary:")
    for level, count in counts.items():
        print(f"- {level}: {count}")

    if counts["ERROR"]:
        print("Important: even one ERROR line should trigger investigation in embedded QA.")


if __name__ == "__main__":
    main()