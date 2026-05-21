import requests
import pytest


def test_1():
    response = requests.get(url="http://127.0.0.1:8000/items")
    assert response.status_code == 200, "wrong status code"


def test_2():
    response = requests.get(url="http://127.0.0.1:8000/items")
    assert response.status_code == 200, "wrong status code"

@pytest.mark.usefixtures("log_time")
class TestClass1():
    def test_3(self):
        response = requests.get(url="http://127.0.0.1:8000/items")
        assert response.status_code == 200, "wrong status code"


    def test_4(self):
        response = requests.get(url="http://127.0.0.1:8000/items")
        assert response.status_code == 200, "wrong status code"