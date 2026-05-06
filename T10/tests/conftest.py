from pathlib import Path
from .helpers import execute_command
import pytest


PROJECT_ROOT = Path(__file__).resolve().parents[1]
APPLICATION_DIR = PROJECT_ROOT / "application"


@pytest.fixture(scope="session")
def application_dir() -> Path:
	return APPLICATION_DIR


@pytest.fixture(scope="session")
def calculator_script(application_dir: Path) -> Path:
	return application_dir / "b_calc"

@pytest.fixture(scope="function")
def run_calc(calculator_script: Path):
    # Keep each test focused on inputs and expected output.
    def _run(operator: str, left: str, right: str) -> str:
        return execute_command(calculator_script, operator, left, right)
    return _run



@pytest.fixture(scope="function")
def f_function():
    dict1 = {"ccc":333, "ddd": 444}
    print(f"⚠️ {f_function.__name__}")
    return dict1

@pytest.fixture(scope="class")
def f_class():
    print(f"⚠️ ⚠️ {f_class.__name__}")
    return f_class.__name__

@pytest.fixture(scope="module")
def f_module():
    print(f"⚠️ ⚠️ ⚠️ {f_module.__name__}")
    return f_module.__name__

@pytest.fixture(scope="package")
def f_package():
    print(f"⚠️ ⚠️ ⚠️ ⚠️ {f_package.__name__}")
    return f_package.__name__

@pytest.fixture(scope="session")
def f_session():
    dict1 = {"aaa":111, "bbb": 222}
    print(f"⚠️ ⚠️ ⚠️ ⚠️ ⚠️ {f_session.__name__}")
    return dict1



"""
conftest.py
Pytest discovers it automatically.
Typical uses:
    fixtures
    hooks
    shared test setup
    shared teardown
    test data paths
    custom pytest behavior for one test subtree
"""
