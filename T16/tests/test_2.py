import pytest

import app.app1 as app_module


@pytest.fixture
def isolated_items_db(monkeypatch):
    """Reset in-memory DB for each test so tests are deterministic."""
    seed = {
        1: {"id": 1, "name": "Laptop", "price": 999.99},
        2: {"id": 2, "name": "Monitor", "price": 349.00},
    }
    monkeypatch.setattr(app_module, "items_db", seed.copy())
    return app_module.items_db


# ------------------------
# create_item (/items POST)
# ------------------------

def test_create_item_edge_empty_body_returns_422(client, isolated_items_db):
    response = client.post("/items", json={})
    assert response.status_code == 422


def test_create_item_edge_null_body_returns_422(client, isolated_items_db):
    response = client.post("/items", json=None)
    assert response.status_code == 422


def test_create_item_boundary_min_valid_values_returns_201(client, isolated_items_db):
    payload = {"id": 3, "name": "A", "price": 0.01}
    response = client.post("/items", json=payload)
    assert response.status_code == 201
    assert response.json() == payload


def test_create_item_boundary_price_zero_returns_422(client, isolated_items_db):
    payload = {"id": 3, "name": "A", "price": 0}
    response = client.post("/items", json=payload)
    assert response.status_code == 422


def test_create_item_error_duplicate_id_returns_409(client, isolated_items_db):
    payload = {"id": 1, "name": "Dup", "price": 10.0}
    response = client.post("/items", json=payload)
    assert response.status_code == 409


# ---------------------
# list_items (/items GET)
# ---------------------

def test_list_items_edge_default_no_input_returns_seed_data(client, isolated_items_db):
    response = client.get("/items")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 2


def test_list_items_edge_empty_store_returns_empty_list(client, monkeypatch):
    monkeypatch.setattr(app_module, "items_db", {})
    response = client.get("/items")
    assert response.status_code == 200
    assert response.json() == []


def test_list_items_boundary_pretty_true_returns_indented_json(client, isolated_items_db):
    response = client.get("/items?pretty=true")
    assert response.status_code == 200
    assert "\n" in response.text
    assert response.headers["content-type"].startswith("application/json")


def test_list_items_error_invalid_pretty_value_returns_422(client, isolated_items_db):
    response = client.get("/items?pretty=not_bool")
    assert response.status_code == 422


# -------------------------
# get_item (/items/{id} GET)
# -------------------------

def test_get_item_boundary_existing_lowest_id_returns_200(client, isolated_items_db):
    response = client.get("/items/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1


def test_get_item_boundary_zero_id_returns_404(client, isolated_items_db):
    response = client.get("/items/0")
    assert response.status_code == 404


def test_get_item_edge_null_like_path_value_returns_422(client, isolated_items_db):
    response = client.get("/items/null")
    assert response.status_code == 422


def test_get_item_error_not_found_returns_404(client, isolated_items_db):
    response = client.get("/items/999")
    assert response.status_code == 404
