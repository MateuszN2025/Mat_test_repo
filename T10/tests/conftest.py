from pathlib import Path

import pytest


PROJECT_ROOT = Path(__file__).resolve().parents[1]
APPLICATION_DIR = PROJECT_ROOT / "application"


@pytest.fixture
def application_dir() -> Path:
	return APPLICATION_DIR


@pytest.fixture
def calculator_script(application_dir: Path) -> Path:
	return application_dir / "b_calc"

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
