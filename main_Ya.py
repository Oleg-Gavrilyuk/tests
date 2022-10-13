import requests

token = ''


def get_headers():
    return {
        'Content-Type': 'application/json',
        'Authorization': 'OAuth {}'.format(token)
    }


def create_folder():
    url = "https://cloud-api.yandex.net/v1/disk/resources"
    headers = get_headers()
    params = {"path": "test"}
    response = requests.put(url, headers=headers, params=params)
    return response.status_code