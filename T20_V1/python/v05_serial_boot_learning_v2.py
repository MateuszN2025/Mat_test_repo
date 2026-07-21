"""Basic serial port learning: connect and read data.

Run:
    python3 T20_V/python/v05_serial_boot_learning_v2.py

Real hardware example (uncomment and adjust port/baud):
    ser = serial.Serial("/dev/ttyUSB0", baudrate=115200, timeout=1)
"""

from __future__ import annotations

try:
    import serial
except ImportError:
    serial = None
import w_r
from pathlib import Path


# --- Fake port to simulate a real serial device (no hardware needed) ---

class FakeSerialPort:
    def __init__(self, lines: list[bytes]) -> None:
        self._lines = lines
        self._index = 0

    def readline(self) -> bytes:
        if self._index >= len(self._lines):
            return b""
        line = self._lines[self._index]
        self._index += 1
        return line

    def close(self) -> None:
        pass  # nothing to close for a fake port


# --- Main: open port and read lines ---

# @w_r
def main() -> None:
    port = FakeSerialPort([
        b"boot: power good\n",
        b"kernel: init done\n",
        b"system ready\n",
    ])
    # port2 = serial.Serial("/dev/ttyUSB0", baudrate=115200, timeout=1)
    # port2.readlines()

    # With real hardware it would look like:
    #   port = serial.Serial("/dev/ttyUSB0", baudrate=115200, timeout=1)

    print("Reading from serial port...\n")

    dir = Path(__file__).parents[0]
    print("------------------------------------------")
    print(dir)
    print("------------------------------------------")  
    # path object (a string-like reference to where the file would be). 
    new_file: Path = dir / "v05_logs_from_serial.txt"

    if not new_file.exists():
        new_file.touch()  # create empty file once
        print(f"log file created: {new_file}")

    with open(new_file, "w") as f:  # "a" = append, never overwrites existing content
        for _ in range(10):  # read up to 10 lines
            raw = port.readline()
            if not raw:
                break  # no more data

            # decode bytes -> string, strip newline
            line = raw.decode("utf-8")
            f.write(line)
            print(f"received: {line}")

    port.close()
    print("\nDone.")


if __name__ == "__main__":
    main()
