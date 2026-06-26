"""Short learning file for requests-based device checks.

Run:
    python3 T20_V/python/06_requests_learning.py

Optional:
    pip install requests
"""

from __future__ import annotations

from dataclasses import dataclass
import w_r

try:
    import requests
except ImportError:  # pragma: no cover - learning fallback for missing dependency.
    requests = None


@dataclass
class FakeResponse:
    status_code: int
    payload: dict[str, str]

    def json(self) -> dict[str, str]:
        return self.payload


class FakeSession:
    def get(self, url: str, timeout: int) -> FakeResponse:
        print(f"GET {url} with timeout={timeout}")
        return FakeResponse(status_code=200, payload={"status": "healthy", "fw": "1.2.3"})


def check_device_health(session: object, base_url: str) -> int:
    response = session.get(f"{base_url}/health", timeout=3)
    print(f"status code: {response.status_code}")
    payload = response.json()
    print(f"payload: {payload}")

    if response.status_code != 200:
        return 1
    if payload.get("status") != "healthy":
        return 2
    return 0

@w_r
def main() -> int:
    session = FakeSession()
    exit_code = check_device_health(session, "http://device-under-test")
    if requests is None:
        print("Note: requests is not installed, so this run used a fake session for learning.")
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())