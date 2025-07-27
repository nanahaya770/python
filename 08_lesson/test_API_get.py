import requests


BEARER_TOKEN = (
    '770'
)
URL = (
    'https://yougile.com/api-v2/projects/'
    '602a205a-34d8-4cc9-9123-50fbea4ddc02'
)


def test_get_project_by_id():  # позитивный тест
    HEADERS = {
        'Authorization': f'Bearer {BEARER_TOKEN}',
        'Content-Type': 'application/json'
    }
    response = requests.get(URL, headers=HEADERS)
    assert response.status_code == 200


def test_get_project_by_id_no_auth():  # Негативный тест
    HEADERS = {
        'Content-Type': 'application/json'
    }
    response = requests.get(URL, headers=HEADERS)
    assert response.status_code == 401
