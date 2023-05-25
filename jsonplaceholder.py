import pytest
import requests
import json

def test_get_users_status_code_200(base_url_3):
    response = requests.get(f"{base_url_3}/users")
    assert response.status_code == 200

@pytest.mark.parametrize("post_id", [1, 5, 50],
                         ids=["one_post", "five_post", "fifty_post"])
def test_check_id_post(post_id, base_url_3):
    response = requests.get(f"{base_url_3}/posts/{post_id}")
    assert response.status_code == 200
    assert response.json()["id"] == post_id

@pytest.mark.parametrize("post", [1, 6, 60])
def test_delete_post(post, base_url_3):
    response = requests.delete(f"{base_url_3}/posts/{post}")
    assert response.status_code == 200

def test_delete_resource():
    url = 'https://jsonplaceholder.typicode.com/posts/1'
    headers = {'Content-Type': 'application/json'}
    payload = {"id": 101}
    response = requests.delete(url, headers=headers, json=payload)
    assert response.status_code == 200
    assert response.text == '{}'

def test_check_quantity_post_100(base_url_3):
    response = requests.get(f"{base_url_3}/posts")
    assert len(response.json()) == 100
    assert response.status_code == 200
