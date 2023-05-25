import requests
import pytest

def test_status_code(base_url_2):
    response = requests.get(base_url_2)
    assert response.status_code == 200

@pytest.mark.parametrize("count", [1, 100, 200],
                         ids=['one_breweries_list', 'one_hundred_breweries_list',
                              'two_hundred_breweries_list'])
def test_count_number_of_breweries(count, base_url_2):
    response = requests.get(f"{base_url_2}/v1/breweries?per_page={count}")
    assert response.json()
    assert response.status_code == 200
    assert len(response.json()) == count


@pytest.mark.parametrize("type_breweries",
                         ["micro", "nano", "regional", "brewpub", "large", "planning", "bar", "contract", "proprietor",
                          "closed"],
                         ids=["micro_breweries", "nano_breweries", "regional_breweries", "brewpub_breweries",
                              "large_breweries", "planning_breweries", "bar_breweries", " contract_breweries",
                              "proprietor_breweries", "closed_breweries"])
def test_get_types_breweries(type_breweries, base_url_2):
    response = requests.get(f"{base_url_2}/v1/breweries?by_type={type_breweries}&per_page=10")
    assert response.json()
    assert response.status_code == 200
    for brewery in response.json():
        assert brewery.get("brewery_type") == type_breweries


@pytest.mark.parametrize("id", [1, 234])
def test_negative_list(base_url_2, id):
    url = requests.get(f"{base_url_2}/breweries/{id}")
    assert url.status_code == 404

expected_params = [
    "id",
    "name",
    "brewery_type",
    "address_1",
    "address_2",
    "address_3",
    "city",
    "state_province",
    "postal_code",
    "country",
    "longitude",
    "latitude",
    "phone",
    "website_url",
    "state",
    "street"
]

@pytest.mark.parametrize("param", expected_params)
def test_get_all_breweries(param, base_url_2):
    response = requests.get(f"{base_url_2}/v1/breweries")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0
    for brewery in data:
        assert param in brewery