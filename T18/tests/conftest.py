import os
import signal
import socket
import subprocess
import time
import pytest
from pathlib import Path
from typing import Dict, Any

# Path resolution
file_name = Path(__file__).resolve()
folder_dir = file_name.parents[1]

def connection_check_helper(host: str, port: int, process: subprocess.Popen) -> None:
    """Poll until the server is accepting connections (max 10 s)."""
    for _ in range(20):
        try:
            with socket.create_connection((host, port), timeout=0.5):
                break
        except OSError:
            time.sleep(0.5)
    else:
        # Loop finished without breaking; server failed to start
        if process.poll() is None:
            os.killpg(os.getpgid(process.pid), signal.SIGKILL) # Changed from SIGTERM
            process.wait()
        raise RuntimeError(f"App did not start on {host}:{port}")

# Tests run: Because run_app is marked with autouse=True,
# this entire setup chain will happen automatically before any tests execute, 
# even if the tests do not explicitly request the run_app fixture.
# 
# Pytest defaults to scope="function". This means Pytest
# would execute the fixture setup and teardown for every single test.
# If you have 50 tests, your code would start the API server, wait for it to boot,
# run one test, kill the server, and repeat 50 times.

# wider scope fixture (session) tried to use
# narrower scope fixture (function)

# ---------------------------------------------
# function < class < module < package < session
# ---------------------------------------------


@pytest.fixture(scope="package")
def app_config() -> Dict[str, Any]:
    return {
        "host": "127.0.0.1",
        "port": 8000,
        "endpoint": "/items",
    }

@pytest.fixture(scope="module", autouse=True)
def run_app(app_config: Dict[str, Any]):
    host = app_config["host"]
    port = app_config["port"]
    endpoint = app_config['endpoint']    
    app_config["url"] = f"http://{host}:{port}{endpoint}"
    
    # Use pathlib to safely construct the script path
    script_path = str(folder_dir / "tests" / "r_api.sh")
    
    process = subprocess.Popen(
        args=["bash", script_path],
        start_new_session=True,
        env={
            **os.environ,
            "APP_HOST": host,
            "APP_PORT": str(port),
        }
    )

    connection_check_helper(host, port, process)
    print(f"\n[➖SETUP➖] Server is up on {host}:{port}!✅\n")
    yield app_config
    print("\n[➖TEARDOWN➖] Killing server...❌")
    # Teardown: Kill the entire process group
    if process.poll() is None:
        os.killpg(os.getpgid(process.pid), signal.SIGKILL) # Changed from SIGTERM
        process.wait()
    print("\n[➖TEARDOWN➖] Server killed.❗")

@pytest.fixture(scope="function")
def log_time():
    t1 = time.perf_counter_ns()
    yield
    t2 = time.perf_counter_ns()
    td = t2 - t1
    print(f"\n ⚠️  DELTA TIME: {(td/1e6):.0f} ms ⚠️ ")

# @pytest.fixture
# def url1(app_config: Dict[str, Any]) -> str:
#     # Build the URL dynamically from the config rather than hardcoding
#     return f"http://{app_config['host']}:{app_config['port']}{app_config['endpoint']}"


"""
All built-in scope options and their range:

function
Range: one test function call.
Created: before each test that needs it.
Destroyed: right after that test finishes.
Use when: test data must be isolated and fresh every test.

class
Range: all test methods inside one test class.
Created: before the first test method in that class that needs it.
Destroyed: after the last such method in that class.
Use when: class methods can share setup safely (for example one API client config).

module
Range: all tests in one Python module (one test file).
Created: first time needed in that file.
Destroyed: after all tests in that file using it are done.
Use when: setup is expensive but safe to share per file.

package
Range: all tests in one package directory tree (directory with init file).
Created: first time needed in that package.
Destroyed: after package tests complete.
Use when: you want one shared setup across multiple modules in the same package.

session
Range: entire pytest run.
Created: first time needed in the run.
Destroyed: at end of test session.
Use when: very expensive setup (start app/server, DB container, auth token cache).
What matters most in practice:

Wider-scope fixtures cannot depend on narrower-scope fixtures.
Example of invalid dependency: session fixture depends on function fixture.
Valid direction: function fixture can depend on session fixture.
Scope controls both setup frequency and teardown timing.
Quick mental model:

---------------------------------------------
function < class < module < package < session
---------------------------------------------

Moving right means fewer setups, more sharing, more risk of state leakage.
"""
