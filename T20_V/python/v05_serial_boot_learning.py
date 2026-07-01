"""Short learning file for serial-style boot checks.

Run:
    python3 T20_V/python/05_serial_boot_learning.py

Optional:
    pip install pyserial
"""

from __future__ import annotations

from dataclasses import dataclass
import time
import w_r

try:
    import serial
except ImportError:  # pragma: no cover - learning fallback for missing dependency.
    serial = None


@dataclass
class FakeSerialPort:
    lines: list[bytes]
    read_index: int = 0
    writes: list[bytes] | None = None

    def __post_init__(self) -> None:
        if self.writes is None:
            self.writes = []

    def readline(self) -> bytes:
        if self.read_index >= len(self.lines):
            time.sleep(0.1)
            return b""

        line = self.lines[self.read_index]
        self.read_index += 1
        return line

    def write(self, data: bytes) -> None:
        self.writes.append(data)


def wait_for_boot_message(port: FakeSerialPort, expected_text: str, timeout_seconds: float) -> bool:
    deadline = time.monotonic() + timeout_seconds
    while time.monotonic() < deadline:
        line = port.readline().decode("utf-8", errors="replace").strip()
        if not line:
            continue

        print(f"serial read: {line}")
        if expected_text in line:
            return True
    return False


def send_command_with_retry(
    port: FakeSerialPort,
    command: str,
    expected_response: str,
    timeout_seconds: float,
    retries: int,
) -> bool:
    for attempt in range(1, retries + 1):
        print(f"attempt {attempt}: send {command}")
        port.write(f"{command}\n".encode("utf-8"))

        deadline = time.monotonic() + timeout_seconds
        while time.monotonic() < deadline:
            line = port.readline().decode("utf-8", errors="replace").strip()
            if not line:
                continue

            print(f"serial read: {line}")
            if expected_response in line:
                return True
        print("timeout waiting for response, retrying")
    return False


def build_demo_port() -> FakeSerialPort:
    return FakeSerialPort(
        lines=[
            b"bootrom: power good\n",
            b"kernel: starting services\n",
            b"system boot completed\n",
            b"status=busy\n",
            b"status=ready\n",
        ]
    )

@w_r
def main() -> int:
    demo_port = build_demo_port()
    boot_ok = wait_for_boot_message(demo_port, "boot completed", timeout_seconds=2)
    if not boot_ok:
        print("FAIL: boot message not detected")
        return 1

    command_ok = send_command_with_retry(
        demo_port,
        command="status",
        expected_response="ready",
        timeout_seconds=0.5,
        retries=2,
    )
    if not command_ok:
        print("FAIL: device command did not produce expected response")
        return 2

    print("PASS: serial boot flow matched expected behavior")
    if serial is None:
        print("Note: pyserial is not installed, so this run used a fake port for learning.")
    jlk
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
