"""Short learning file for pytest fixture scope and parameterization.

Run:
    python3 -m pytest -q T20_V/python/11_pytest_parametrize_scope_learning.py
"""

from __future__ import annotations

from dataclasses import dataclass

import pytest


@dataclass
class FakeCamera:
    name: str
    firmware: str
    online: bool


@pytest.fixture(scope="module")
def lab_config() -> dict[str, str]:
    # Module scope matches setup that is expensive but shared by several tests.
    return {"site": "lab-a", "expected_fw": "1.2.3"}


@pytest.fixture
def camera_factory(lab_config: dict[str, str]):
    def make_camera(name: str, online: bool = True) -> FakeCamera:
        return FakeCamera(name=name, firmware=lab_config["expected_fw"], online=online)

    return make_camera


@pytest.mark.parametrize("camera_name", ["front-door", "warehouse", "server-room"])
def test_camera_comes_online(camera_factory, camera_name: str) -> None:
    camera = camera_factory(camera_name)
    assert camera.online is True, f"{camera.name} should be reachable after boot"


@pytest.mark.parametrize(
    ("camera_name", "firmware", "expected"),
    [
        ("front-door", "1.2.3", True),
        ("warehouse", "1.2.2", False),
    ],
)
def test_firmware_validation(camera_factory, camera_name: str, firmware: str, expected: bool) -> None:
    camera = camera_factory(camera_name)
    camera.firmware = firmware
    matches = camera.firmware == "1.2.3"
    assert matches is expected