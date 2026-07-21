"""Short pytest examples for embedded smoke learning.

Run:
    python3 -m pytest -q T20_V/tests/test_embedded_smoke_pytest.py
"""

from __future__ import annotations

import pytest

from T20_V.python.fake_device_model import FakeDevice, is_ready_for_smoke


@pytest.fixture
def healthy_device() -> FakeDevice:
    # A fixture keeps the starting test state explicit and reusable.
    return FakeDevice(
        hostname="camera-01",
        firmware_version="1.2.3",
        online=True,
        main_service_healthy=True,
        sensor_streaming=True,
    )


def test_device_is_ready_when_all_critical_signals_are_healthy(healthy_device: FakeDevice) -> None:
    assert is_ready_for_smoke(healthy_device) is True


@pytest.mark.parametrize(
    ("field_name", "expected_problem"),
    [
        ("online", "device unreachable"),
        ("main_service_healthy", "critical service unhealthy"),
        ("sensor_streaming", "sensor pipeline inactive"),
    ],
)
def test_device_is_not_ready_when_any_critical_signal_fails(
    healthy_device: FakeDevice,
    field_name: str,
    expected_problem: str,
) -> None:
    setattr(healthy_device, field_name, False)

    # The assertion message is important because CI failures should be easy to diagnose.
    assert is_ready_for_smoke(healthy_device) is False, expected_problem


def test_health_status_exposes_firmware_version(healthy_device: FakeDevice) -> None:
    status = healthy_device.health_status()
    assert status["firmware_version"] == "1.2.3"