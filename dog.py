import requests
import pytest


def test_get_breed():
    response = requests.get("https://dog.ceo/api/breeds/list/all")
    assert response.status_code == 200
    data = response.json()
    assert "shiba" in data["message"]
    assert "status" in data
    assert data["status"] == "success"

@pytest.mark.parametrize('count', [1, 9, 40], ids=['one_message', 'nine_messages', 'forty_messages'])
def test_count_number_of_messages(count,base_url):
    response = requests.get(f"{base_url}/breeds/image/random/{count}")
    assert response.status_code == 200
    assert response.json()
    assert len(response.json()["message"]) == count

@pytest.mark.parametrize('count', [1, 9, 40], ids=['one_message', 'nine_messages', 'forty_messages'])
def test_200_success_code_response(count,base_url):
    response = requests.get(f"{base_url}/breeds/image/random/{count}")
    assert response.status_code == 200
    assert response.json()
    assert response.json()["status"] == "success"

@pytest.mark.parametrize("breed_name, status_code", [("shiba", 200)])
def test_dog_breed_image(breed_name, status_code,base_url):
    response = requests.get(f"{base_url}/breed/{breed_name}/images/random")
    assert response.status_code == status_code

def test_dog_breed_images_contain_name():
    response = requests.get("https://dog.ceo/api/breed/hound/blood/images")
    assert response.status_code == 200
    for data in response.json()["message"]:
        assert "blood" in data, "Отсутствует порода в ссылках с картинками"


