"""Tiny fake embedded device model for pytest learning.

This file exists so the pytest examples test behavior instead of shell commands only.
"""

from __future__ import annotations

from dataclasses import dataclass
import w_r


@dataclass
class FakeDevice:
    hostname: str = "host"
    firmware_version: str = "v1.1"
    online: bool = True
    main_service_healthy: bool = True
    sensor_streaming: bool = True

    def health_status(self) -> dict[str, str | bool]:
        # Returning structured data makes assertions clearer than parsing raw strings.
        return {
            "hostname": self.hostname,
            "firmware_version": self.firmware_version,
            "online": self.online,
            "main_service_healthy": self.main_service_healthy,
            "sensor_streaming": self.sensor_streaming,
        }


def is_ready_for_smoke(device: FakeDevice) -> bool:
    status = device.health_status()
    print(status)
    # Smoke checks should be simple and high-signal.
    return bool(
        status["online"]
        and status["main_service_healthy"]
        and status["sensor_streaming"]
    )
    
@w_r
def main():
    f1 = FakeDevice()
    is_ready_for_smoke(f1)
    
if __name__ == "__main__":
    main()