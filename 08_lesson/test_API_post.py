import requests


BEARER_TOKEN = (
    '770'
)
URL = 'https://yougile.com/api-v2/projects'

HEADERS = {
    'Authorization': f'Bearer {BEARER_TOKEN}',
    'Content-Type': 'application/json'
}


def test_post_project():  # позитивный тест
    body = {
            "title": "Пример проекта",
            "users": {
                "ae5c4880-ef80-46c4-9821-2241ab65c022": "admin"
            }

    }
    response = requests.post(URL, headers=HEADERS, json=body)
    assert response.status_code == 201


def test_post_project_empty_title():  # негативный тест
    body = {
            "title": "",
            "users": {
                "ae5c4880-ef80-46c4-9821-2241ab65c022": "admin"
            }

    }
    response = requests.post(URL, headers=HEADERS, json=body)
    assert response.status_code == 400
