import pytest
import json
import requests

@pytest.fixture()
def base_url():
    return "https://dog.ceo/api"

@pytest.fixture()
def base_url_2():
    return "https://api.openbrewerydb.org"

@pytest.fixture()
def base_url_3():
    return "https://jsonplaceholder.typicode.com"

def pytest_addoption(parser):
    parser.addoption("--url", action="store", default="https://ya.ru")
    parser.addoption("--status_code", action="store", type=int, default=200)

@pytest.fixture
def url(request):
    return request.config.getoption("--url")

@pytest.fixture
def status_code(request):
    return request.config.getoption("--status_code")