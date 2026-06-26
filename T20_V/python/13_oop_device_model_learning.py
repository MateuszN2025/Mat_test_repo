"""Short learning file for OOP device models.

Run:
    python3 T20_V/python/13_oop_device_model_learning.py
"""

from __future__ import annotations

from abc import ABC, abstractmethod


class EmbeddedDevice(ABC):
    def __init__(self, name: str) -> None:
        self.name = name
        self.powered_on = False

    def turn_on(self) -> None:
        self.powered_on = True

    @abstractmethod
    def get_status(self) -> str:
        raise NotImplementedError


class Camera(EmbeddedDevice):
    def __init__(self, name: str, stream_running: bool) -> None:
        super().__init__(name)
        self.stream_running = stream_running

    def get_status(self) -> str:
        if not self.powered_on:
            return "offline"
        return "streaming" if self.stream_running else "booted-no-stream"


class Alarm(EmbeddedDevice):
    def __init__(self, name: str, armed: bool) -> None:
        super().__init__(name)
        self.armed = armed

    def get_status(self) -> str:
        if not self.powered_on:
            return "offline"
        return "armed" if self.armed else "disarmed"


def main() -> int:
    devices: list[EmbeddedDevice] = [
        Camera(name="camera-front", stream_running=True),
        Alarm(name="alarm-lobby", armed=False),
    ]

    for device in devices:
        device.turn_on()
        print(f"{device.name}: {device.get_status()}")

    print("Interview note: tests should call small device methods instead of duplicating transport logic.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())