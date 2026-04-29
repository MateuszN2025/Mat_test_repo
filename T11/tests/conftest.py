from pathlib import Path
import os

import pytest


PROJECT_ROOT = Path(__file__).resolve().parents[1]
APPLICATION_DIR = PROJECT_ROOT / "application"


@pytest.fixture
def application_dir() -> Path:
	return APPLICATION_DIR

@pytest.fixture
def calculator_script(application_dir: Path) -> Path:
	return application_dir / "b_calc"

@pytest.fixture
def project_root() -> Path:
	return PROJECT_ROOT


@pytest.fixture
def remote_calc_command() -> list[str]:
    """Build remote calculator command from environment variables.

    Required:
    - CALC_SSH_PASSWORD

    Optional (with defaults):
    - CALC_SSH_USER (default: vboxuser1)
    - CALC_SSH_HOST (default: 192.168.0.152)
    - CALC_REMOTE_PATH (default: /home/vboxuser1/calc2/b_calc)
    """
    password = os.getenv("CALC_SSH_PASSWORD")
    if not password:
        pytest.skip("Set CALC_SSH_PASSWORD to run remote calculator tests")

    user = os.getenv("CALC_SSH_USER")
    host = os.getenv("CALC_SSH_HOST")
    remote_path = os.getenv("CALC_REMOTE_PATH")

    return ["sshpass", "-p", password, "ssh", f"{user}@{host}", remote_path]

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
