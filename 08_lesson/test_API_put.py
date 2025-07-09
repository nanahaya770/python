import requests


BEARER_TOKEN = (
    '770'
)
URL = (
    'https://yougile.com/api-v2/projects/'
    '602a205a-34d8-4cc9-9123-50fbea4ddc02'
)

HEADERS = {
    'Authorization': f'Bearer {BEARER_TOKEN}',
    'Content-Type': 'application/json'
}


def test_put_project_by_id():  # позитивный тест
    URL = (
        'https://yougile.com/api-v2/projects/'
        '602a205a-34d8-4cc9-9123-50fbea4ddc02'
    )
    body = {
            "title": "770",
            "users": {
                "ae5c4880-ef80-46c4-9821-2241ab65c022": "admin"
            }

    }
    response = requests.put(URL, headers=HEADERS, json=body)
    assert response.status_code == 200


def test_put_project_by_no_id():  # негативный тест
    URL = 'https://yougile.com/api-v2/projects'
    response = requests.put(URL, headers=HEADERS)
    assert response.status_code == 404
