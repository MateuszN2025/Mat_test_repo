"""Short learning file for BDD step mapping.

Run:
    python3 T20_V/python/12_bdd_step_mapping_learning.py
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class DeviceWorld:
    firmware_installed: bool = False
    powered_on: bool = False
    health_ok: bool = False
    service_ok: bool = False


def given_expected_firmware_installed(world: DeviceWorld) -> None:
    world.firmware_installed = True


def when_device_is_powered_on(world: DeviceWorld) -> None:
    if not world.firmware_installed:
        raise RuntimeError("firmware must be installed before power-on")
    world.powered_on = True
    world.health_ok = True
    world.service_ok = True


def then_device_responds_to_health_check(world: DeviceWorld) -> None:
    assert world.health_ok is True


def then_main_service_is_healthy(world: DeviceWorld) -> None:
    assert world.service_ok is True


def main() -> int:
    world = DeviceWorld()
    scenario_steps = [
        ("Given", "a test device with the expected firmware installed", given_expected_firmware_installed),
        ("When", "the device is powered on", when_device_is_powered_on),
        ("Then", "the device should respond to a health check within 30 seconds", then_device_responds_to_health_check),
        ("And", "the main service should report a healthy state", then_main_service_is_healthy),
    ]

    for keyword, text, step_function in scenario_steps:
        print(f"{keyword} {text}")
        step_function(world)

    print("PASS: scenario steps mapped cleanly to Python functions")
    print("Interview note: behave and pytest-bdd wrap this same idea with decorators and feature files.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())