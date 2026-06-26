"""Short learning file for threading in device polling.

Run:
    python3 T20_V/python/08_threading_learning.py
"""

from __future__ import annotations

from dataclasses import dataclass
import queue
import threading
import time
import w_r


@dataclass
class DeviceResult:
    name: str
    status: str


def poll_device(name: str, delay_seconds: float, results: queue.Queue[DeviceResult]) -> None:
    time.sleep(delay_seconds)
    results.put(DeviceResult(name=name, status="healthy"))

@w_r
def main() -> int:
    result_queue: queue.Queue[DeviceResult] = queue.Queue()
    threads = [
        threading.Thread(target=poll_device, args=("camera-1", 0.2, result_queue)),
        threading.Thread(target=poll_device, args=("sensor-2", 0.1, result_queue)),
    ]

    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

    while not result_queue.empty():
        result = result_queue.get()
        print(f"{result.name}: {result.status}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())