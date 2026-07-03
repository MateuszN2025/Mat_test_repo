# ─── SUBPROCESS ───────────────────────────────────────────────────────────────
import shlex, subprocess
result = subprocess.run(shlex.split("python3 --version"),
                        text=True, capture_output=True, check=False, timeout=5)
result.returncode  # 0 = ok
result.stdout.strip()

# ─── PATHLIB + LOGGING + ARGPARSE ─────────────────────────────────────────────
import argparse, logging
from pathlib import Path

logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")

parser = argparse.ArgumentParser()
parser.add_argument("--log-file", type=Path, default=Path("/tmp/device.log"))
parser.add_argument("--expected-text", default="boot completed")
args = parser.parse_args()

log_file: Path = args.log_file
content = log_file.read_text(encoding="utf-8")   # Path.read_text()
log_file.exists()                                  # Path.exists()

# ─── LOG PARSING ──────────────────────────────────────────────────────────────
from collections import Counter

lines = ["INFO boot ok", "WARNING weak signal", "ERROR stream failed"]
counts: Counter = Counter(line.split()[0] for line in lines)
# Counter({'INFO': 1, 'WARNING': 1, 'ERROR': 1})

# ─── REGEX + JSON + CSV ───────────────────────────────────────────────────────
import re, json, csv

pattern = re.compile(r"(ERROR|Kernel panic|watchdog reset)")
failures = [l for l in lines if pattern.search(l)]

summary = json.loads('{"status": "pass"}')           # str → dict
Path("out.json").write_text(json.dumps(summary))      # dict → file

with open("results.csv", newline="") as fh:
    rows = list(csv.DictReader(fh))                   # list[dict]

# ─── HTTP HEALTH CHECK (requests) ─────────────────────────────────────────────
import requests

resp = requests.get("http://device/health", timeout=3)
assert resp.status_code == 200
assert resp.json()["status"] == "healthy"

# ─── SSH TO DEVICE (paramiko) ─────────────────────────────────────────────────
import paramiko

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect("192.168.1.10", username="admin", password="secret")
_, stdout, _ = client.exec_command("systemctl is-active app")
output = "".join(stdout.readlines()).strip()   # "active"
client.close()

# ─── THREADING (poll multiple devices in parallel) ─────────────────────────────
import threading, queue, time
from dataclasses import dataclass

@dataclass
class DeviceResult:
    name: str
    status: str

def poll_device(name: str, delay: float, q: "queue.Queue[DeviceResult]") -> None:
    time.sleep(delay)
    q.put(DeviceResult(name, "healthy"))

result_q: queue.Queue[DeviceResult] = queue.Queue()
threads = [
    threading.Thread(target=poll_device, args=("camera-1", 0.2, result_q)),
    threading.Thread(target=poll_device, args=("sensor-2", 0.1, result_q)),
]
for t in threads: t.start()
for t in threads: t.join()
while not result_q.empty():
    print(result_q.get())

# ─── MULTIPROCESSING (parallel log analysis) ──────────────────────────────────
from multiprocessing import Pool

LOG_CHUNKS = ["INFO ok\nERROR fail\n", "INFO ok\n"]

def count_errors(chunk: str) -> int:
    return sum(1 for l in chunk.splitlines() if l.startswith("ERROR"))

with Pool(processes=2) as pool:
    error_counts = pool.map(count_errors, LOG_CHUNKS)   # [1, 0]

# ─── OOP DEVICE MODEL (ABC) ───────────────────────────────────────────────────
from abc import ABC, abstractmethod

class EmbeddedDevice(ABC):
    def __init__(self, name: str) -> None:
        self.name = name
        self.powered_on = False

    def turn_on(self) -> None:
        self.powered_on = True

    @abstractmethod
    def get_status(self) -> str: ...

class Camera(EmbeddedDevice):
    def get_status(self) -> str:
        return "streaming" if self.powered_on else "offline"

# ─── DECORATORS + GENERATORS ──────────────────────────────────────────────────
from functools import wraps
from collections.abc import Callable, Iterator

def log_step(name: str) -> Callable:
    def decorator(fn: Callable) -> Callable:
        @wraps(fn)
        def wrapper(*args, **kwargs):
            print(f"START {name}")
            result = fn(*args, **kwargs)
            print(f"END {name}")
            return result
        return wrapper
    return decorator

def sensor_stream() -> Iterator[int]:
    for v in [18, 19, 20]: yield v

@log_step("read sensor")
def get_latest() -> int:
    return max(sensor_stream())   # drives the generator to completion

# ─── PYTEST FIXTURES ──────────────────────────────────────────────────────────
import pytest

@dataclass
class FakeDevice:
    name: str
    booted: bool
    firmware: str

@pytest.fixture
def device() -> FakeDevice:
    return FakeDevice("camera-1", booted=True, firmware="1.2.3")

def test_is_booted(device: FakeDevice) -> None:
    assert device.booted is True

# ─── PYTEST PARAMETRIZE + SCOPE ───────────────────────────────────────────────
@pytest.fixture(scope="module")        # created once per module (expensive setup)
def lab_config() -> dict:
    return {"expected_fw": "1.2.3"}

@pytest.mark.parametrize("name", ["front-door", "warehouse", "server-room"])
def test_camera_online(name: str) -> None:
    assert name  # replace with real check

@pytest.mark.parametrize(("fw", "ok"), [("1.2.3", True), ("1.2.2", False)])
def test_firmware(fw: str, ok: bool) -> None:
    assert (fw == "1.2.3") is ok

# ─── BDD STEP MAPPING ─────────────────────────────────────────────────────────
# Feature file (Gherkin):
#   Scenario: Device boots and becomes reachable
#     Given a test device with the expected firmware installed
#     When the device is powered on
#     Then the device should respond to a health check within 30 seconds
#     And the main service should report a healthy state

@dataclass
class DeviceWorld:
    firmware_installed: bool = False
    powered_on: bool = False
    health_ok: bool = False

def given_firmware(world: DeviceWorld) -> None: world.firmware_installed = True
def when_power_on(world: DeviceWorld) -> None:
    assert world.firmware_installed
    world.powered_on = True
    world.health_ok = True
def then_health(world: DeviceWorld) -> None: assert world.health_ok

# pytest-bdd equivalent:
# from pytest_bdd import given, when, then
# @given("a test device..."); @when("the device is powered on"); @then("health check...")

# ─── BASH CHEATSHEET ──────────────────────────────────────────────────────────
"""
# Strict mode — always use in CI/lab scripts
set -euo pipefail

# Check tool exists
command -v python3 >/dev/null 2>&1 || { echo "missing"; exit 1; }

# Ping smoke check
ping -c 1 "$host" >/dev/null 2>&1 && echo PASS || echo FAIL

# grep / awk / sed on device logs
grep -nE 'ERROR|watchdog reset' /var/log/device.log || true
awk '{count[$1]++} END {for (l in count) print l, count[l]}' device.log
sed -n 's/^INFO service=//p' device.log
tail -n 20 /var/log/device.log

# Network / serial port checks
ip -brief a
ss -ltn
find /dev -maxdepth 1 -name 'ttyUSB*'   # USB-serial adapters

# Background process + cleanup
sleep 30 &; pid=$!; ...; kill "$pid"; wait "$pid" || true

# chmod and exit code
chmod +x script.sh; ./script.sh; echo "exit=$?"

# Export env var for test run
export DEVICE_HOST="192.168.1.10"
"""

# ─── CI QUICK NOTES ───────────────────────────────────────────────────────────
"""
GitHub Actions key ideas:
  on: [push, pull_request]
  jobs:
    test:
      runs-on: ubuntu-latest
      steps:
        - uses: actions/checkout@v4
        - run: pip install -r requirements.txt
        - run: pytest tests/ -v

pytest selection flags:
  pytest -k "smoke"          # by keyword
  pytest -m "smoke"          # by marker
  pytest --co -q             # collect only (dry-run)
  pytest -x                  # stop on first failure
  pytest --tb=short          # shorter tracebacks
"""
