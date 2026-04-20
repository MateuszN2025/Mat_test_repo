import pytest


@pytest.fixture
def sample_data():
    return {
        "name": "Alice",
        "age": 30,
    }


@pytest.fixture
def temp_settings():
    settings = {
        "debug": False,
        "timeout": 5,
    }
    return settings


@pytest.fixture(scope="session")
def app_config():
    return {
        "env": "test",
        "base_url": "http://localhost",
    }

@pytest.fixture
def db_connection():
    connection = {"connected": True}
    yield connection
    connection["connected"] = False