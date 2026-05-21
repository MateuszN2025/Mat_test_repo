import os
import signal
import socket
import subprocess
import time
import pytest
from pathlib import Path

file_name = Path(__file__).resolve()
folder_dir = file_name.parents[1]
repo_dir = file_name.parents[2]

# fuser -k 8000/tcp 2>/dev/null; echo "Port cleared (exit: $?)"
# 
# autouse=True means it runs automatically 
# without needing to be explicitly requested by tests

def connection_check(host, port, process):
    # Poll until the server is accepting connections (max 10 s)
    for _ in range(20):
        try:
            with socket.create_connection((host, port), timeout=0.5):
                break
        except OSError:
            time.sleep(0.5)
    else:
        if process.poll() is None:
            os.killpg(os.getpgid(process.pid), signal.SIGTERM)
            process.wait()
        raise RuntimeError(f"App did not start on {host}:{port}")


@pytest.fixture(scope="session")
def app_config():
    return {
        "host": "127.0.0.1",
        "port": 8000,
        "endpoint": "/items",
    }
    
# In pytest fixtures/tests, the fixture name is replaced
# with its return value, so you can use app_config["host"] directly.

# app_config is a function—but in pytest, when you use it as a fixture, 
# pytest calls the function for you and injects
# its return value (the dictionary) into any test or fixture that requests it.

# @pytest.fixture(scope="session", autouse=True)
@pytest.fixture(scope="session", autouse=True)
def run_app(app_config):
    host = app_config["host"]
    port = app_config["port"]
    process = subprocess.Popen(args=["bash", f"{folder_dir}/tests/r_api.sh"],
                               start_new_session=True,
                               env={
                                   **os.environ,
                                   "APP_HOST": host,
                                   "APP_PORT": str(port),
                               })

    connection_check(host, port, process)

    yield app_config
    # Kill the entire process group (bash + uvicorn child)
    if process.poll() is None:
        os.killpg(os.getpgid(process.pid), signal.SIGTERM)
        process.wait()
    

@pytest.fixture
def url1():
    # return f"http://{run_app['host']}:{run_app['port']}{run_app['endpoint']}"
    return "http://127.0.0.1:8000/items"
    