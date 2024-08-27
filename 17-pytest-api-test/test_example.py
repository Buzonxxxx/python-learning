# Run 'pytest -s -v '

import requests
import pytest

@pytest.fixture
def base_url():
    return "https://jsonplaceholder.typicode.com"

def test_get_request(base_url):
    response = requests.get(f"{base_url}/todos/1")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1

def test_post_request(base_url):
    payload = {
        "name": "John Doe",
        "job": "Software Engineer"
    }
    response = requests.post(f"{base_url}/users", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "John Doe"
    assert data["job"] == "Software Engineer"

def test_put_request(base_url):
    payload = {
        "name": "Jane Smith",
        "job": "QA Engineer"
    }
    response = requests.put(f"{base_url}/users/2", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Jane Smith"
    assert data["job"] == "QA Engineer"

def test_create_user():
    payload = {
        "name": "Jane Smith",
        "job": "QA Engineer"
    }
    response = requests.post("https://reqres.in/api/users", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Jane Smith"
    assert data["job"] == "QA Engineer"
