import sys
from pathlib import Path

import pytest
from fastapi.testclient import TestClient


PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from T15.practice_api.app import create_app
from T15.practice_api.store import InMemoryStore
from T15.tests.page_objects import ItemsApiPage


@pytest.fixture()
def api_page():
    store = InMemoryStore()
    store.reset()
    client = TestClient(create_app())
    yield ItemsApiPage(client)
    store.reset()
