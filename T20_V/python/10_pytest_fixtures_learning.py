"""Short learning file for pytest fixtures.

Run:
    python3 -m pytest -q T20_V/python/10_pytest_fixtures_learning.py
"""

from __future__ import annotations

from dataclasses import dataclass

import pytest


@dataclass
class FakeDevice:
    name: str
    booted: bool
    firmware: str


@pytest.fixture
def fake_device() -> FakeDevice:
    # A fixture keeps setup reusable across many tests.
    return FakeDevice(name="camera-1", booted=True, firmware="1.2.3")


def test_device_is_booted(fake_device: FakeDevice) -> None:
    assert fake_device.booted is True


def test_firmware_version_format(fake_device: FakeDevice) -> None:
    parts = fake_device.firmware.split(".")
    assert len(parts) == 3
    assert all(part.isdigit() for part in parts)