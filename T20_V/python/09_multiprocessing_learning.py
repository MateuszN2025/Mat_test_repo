"""Short learning file for basic multiprocessing.

Run:
    python3 T20_V/python/09_multiprocessing_learning.py
"""

from __future__ import annotations

from multiprocessing import Pool
import w_r


LOG_CHUNKS = [
    "INFO boot completed\nWARNING temperature high\n",
    "INFO app started\nERROR watchdog reset\n",
    "INFO network connected\nERROR ssh failed\n",
]


def count_errors(log_text: str) -> int:
    return sum(1 for line in log_text.splitlines() if line.startswith("ERROR"))

@w_r
def main() -> int:
    with Pool(processes=2) as pool:
        error_counts = pool.map(count_errors, LOG_CHUNKS)

    total_errors = sum(error_counts)
    print(f"error counts per chunk: {error_counts}")
    print(f"total errors: {total_errors}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())