import requests
# import pytest


def test_api_endpoint():
    response = requests.get('https://api.example.com/users')
    assert response.status_code == 200
    assert len(response.json()) > 0


def test_create_user():
    new_user = {
        'name': 'Test User',
        'email': 'test@example.com'
    }
    response = requests.post('https://api.example.com/users', json=new_user)
    assert response.status_code == 201
    assert response.json()['name'] == new_user['name']
