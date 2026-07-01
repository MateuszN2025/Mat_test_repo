"""Short learning file for real pyserial usage.

Run:
    python3 T20_V/python/16_pyserial_real_port_learning.py --port /dev/ttyUSB0

Optional:
    pip install pyserial
"""

from __future__ import annotations

import argparse
import time
from typing import Protocol

# package manager name: pyserial
# Python import name: serial

try:
    import serial
except ImportError:  # pragma: no cover - depends on local environment.
    serial = None


class SerialPort(Protocol):
    def readline(self) -> bytes:
        ...

    def write(self, data: bytes) -> int:
        ...

    def flush(self) -> None:
        ...


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Learn how to talk to a device over UART with pyserial")
    parser.add_argument("--port", required=True, help="Serial device path, for example /dev/ttyUSB0")
    parser.add_argument("--baudrate", type=int, default=115200, help="Baud rate for the serial connection")
    parser.add_argument("--read-timeout", type=float, default=0.5, help="Per-read timeout in seconds")
    parser.add_argument("--boot-text", default="boot completed", help="Boot text to wait for")
    parser.add_argument("--command", default="status", help="Command to send after boot")
    parser.add_argument("--expected-response", default="ready", help="Expected text in device response")
    parser.add_argument("--boot-wait", type=float, default=30.0, help="Maximum time to wait for boot text")
    parser.add_argument("--response-wait", type=float, default=5.0, help="Maximum time to wait for command response")
    return parser


def wait_for_text(port: SerialPort, expected_text: str, timeout_seconds: float) -> bool:
    deadline = time.monotonic() + timeout_seconds
    while time.monotonic() < deadline:
        raw_line = port.readline()
        line = raw_line.decode("utf-8", errors="replace").strip()
        if not line:
            continue

        print(f"serial read: {line}")
        if expected_text in line:
            return True
    return False


def send_command_and_verify(
    port: SerialPort,
    command: str,
    expected_response: str,
    timeout_seconds: float,
) -> bool:
    port.write(f"{command}\n".encode("utf-8"))
    port.flush()
    return wait_for_text(port, expected_response, timeout_seconds)


def main() -> int:
    args = build_parser().parse_args()

    if serial is None:
        print("pyserial is not installed. Install it with: pip install pyserial")
        return 2

    try:
        with serial.Serial(args.port, baudrate=args.baudrate, timeout=args.read_timeout) as port:
            print(f"opened serial port: {args.port} at {args.baudrate} baud")

            boot_ok = wait_for_text(port, args.boot_text, args.boot_wait)
            if not boot_ok:
                print("FAIL: boot text was not detected before timeout")
                return 1

            response_ok = send_command_and_verify(
                port,
                command=args.command,
                expected_response=args.expected_response,
                timeout_seconds=args.response_wait,
            )
            if not response_ok:
                print("FAIL: expected response was not detected before timeout")
                return 1

            print("PASS: device booted and responded over UART")
            return 0
    except serial.SerialException as error:
        print(f"FAIL: could not use serial port {args.port}: {error}")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())