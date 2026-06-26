"""Short learning file for decorators and generators.

Run:
    python3 T20_V/python/14_decorators_generators_learning.py
"""

from __future__ import annotations

from collections.abc import Callable, Iterator
from functools import wraps
import time


def log_step(step_name: str) -> Callable[[Callable[..., str]], Callable[..., str]]:
    def decorator(function: Callable[..., str]) -> Callable[..., str]:
        @wraps(function)
        def wrapper(*args, **kwargs) -> str:
            start = time.monotonic()
            print(f"START {step_name}")
            result = function(*args, **kwargs)
            duration = time.monotonic() - start
            print(f"END {step_name} in {duration:.3f}s")
            return result

        return wrapper

    return decorator


def stream_sensor_values() -> Iterator[int]:
    for value in [18, 19, 20, 25]:
        yield value


@log_step("read latest sensor value")
def get_latest_sensor_state() -> str:
    latest_value = None
    for latest_value in stream_sensor_values():
        print(f"sensor value: {latest_value}")
    return f"latest={latest_value}"


def main() -> int:
    state = get_latest_sensor_state()
    print(state)
    print("Interview note: decorators are useful for logging/retry wrappers, generators for streaming sensor data.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())