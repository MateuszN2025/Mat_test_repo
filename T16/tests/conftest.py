import pytest
import sys
from pathlib import Path
from unittest.mock import patch, MagicMock
from fastapi.testclient import TestClient

T16_DIR = Path(__file__).resolve().parents[1]
if str(T16_DIR) not in sys.path:
    sys.path.insert(0, str(T16_DIR))

from app.app1 import app1

@pytest.fixture
def client():
    return TestClient(app1)
    # TestClient is not a fake response mock like unittest.mock.
    # It runs your real FastAPI app code in-process 
    # (router, validation, dependencies, middleware, handlers
    # It skips real network/socket I/O, so it is faster and more stable than hitting localhost.
    # an in-memory HTTP client + transport for your real ASGI app,
    # not a mocked server behavior.
    # 
    # Treat TestClient tests as API component/integration tests, not full E2E.
    # Keep a smaller set of real-network smoke tests to catch deployment/network issues.

@pytest.fixture
def url1():
    return "http://127.0.0.1:8000/items/"


@pytest.fixture
def mock_items():
    # Replaces the ITEMS dict in the app module for the duration of one test.
    # patch() restores the original value automatically after the test ends.
    fake_items = {
        99: {"id": 99, "name": "Mocked Item", "price": 0.01},
    }
    with patch("app.app1.ITEMS", fake_items):
        yield fake_items

