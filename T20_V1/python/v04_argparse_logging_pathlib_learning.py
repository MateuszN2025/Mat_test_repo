"""Short learning file for argparse, pathlib, and logging.

Run:
    python3 T20_V/python/04_argparse_logging_pathlib_learning.py --log-file /tmp/device.log
"""

from __future__ import annotations

import argparse
import logging
from pathlib import Path
import w_r


def build_parser() -> argparse.ArgumentParser:
    # Create the command-line parser object.
    parser = argparse.ArgumentParser(description="Tiny device log checker")
    parser.add_argument(
        "--log-file",
        # Convert the CLI string directly into a pathlib.Path object.
        type=Path, # type=Path makes args.log_file a Path, not a plain string.
        # Use /tmp/device.log if the user does not pass --log-file.
        default=Path("/tmp/device.log"),
        # Help text shown in --help output.
        help="Path to a device log file (default: /tmp/device.log)",
    )
    # Optional argument: text that the script will search for inside the log file.
    parser.add_argument("--expected-text", default="boot completed", help="Text that must exist")
    return parser


def configure_logging() -> None:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")


def check_log_file(log_file: Path, expected_text: str) -> int:
    if not log_file.exists():
        logging.error("Log file not found: %s", log_file)
        return 1

    content = log_file.read_text(encoding="utf-8")
    if expected_text in content:
        logging.info("Found expected text: %s", expected_text)
        return 0

    logging.error("Expected text not found: %s", expected_text)
    return 2

@w_r
def main() -> int:
    configure_logging()
    args = build_parser().parse_args()
    return check_log_file(args.log_file, args.expected_text)


if __name__ == "__main__":
    raise SystemExit(main())
    # main()