import pytest
import requests
import json
import yaml

API_JSON = 'https://d1tjdkfytigl56.cloudfront.net/example-employees.json'
API_YAML = 'https://d1tjdkfytigl56.cloudfront.net/example-employees.yaml'

@pytest.fixture
def api_json_url():
    return API_JSON

def api_yaml_url():
    return API_YAML

def test_api_json_returns_200(api_json_url):
    response = requests.get(api_json_url)
    assert response.status_code == 200

def test_api_returns_valid_json(api_json_url):
    response = requests.get(api_json_url)
    try:
        json_data = json.loads(response.text)
    except ValueError:
        pytest.fail("Response is not valid JSON")

def test_valid_yaml_url():
    url = api_yaml_url()
    response = requests.get(url)
    assert response.status_code == 200, f"Request to {url} failed with status code {response.status_code}"
    try:
        yaml.safe_load(response.content)
    except yaml.YAMLError as e:
        #assert False, f"Response from {url} is not valid YAML: {e}"
        pytest.fail("111Response from {url} is not valid YAML")