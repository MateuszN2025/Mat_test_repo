import requests
import pytest

expected_r = {"id": 1, "name": "Laptop", "price": 999.99}

@pytest.mark.hard
def test_1_get_item_returns_expected_payload(client):
    # With TestClient, base URL is handled internally.
    # http://127.0.0.1:8000
    result = client.get("/items/1")
    print("\n------------------------------------------")
    print(client)
    print("------------------------------------------")
    assert result.status_code == 200
    assert result.json() == expected_r
    
    
@pytest.mark.easy
def test_2_get_item_returns_expected_payload(url1):
    result = requests.get(f"{url1}1")
    assert result.status_code == 200
    assert result.json() == expected_r

@pytest.mark.mock
def test_get_mocked_item(client, mock_items):
    response = client.get("/items/99")
    assert response.status_code == 200
    assert response.json()["name"] == "Mocked Item"

@pytest.mark.mock
def test_real_item_not_in_mock(client, mock_items):
    response = client.get("/items/1")
    assert response.status_code == 404  # original ITEMS is gone during this test
        
