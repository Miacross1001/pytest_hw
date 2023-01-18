import requests

def API_disk(name):
    token_ = ''
    host = 'https://cloud-api.yandex.net/v1/disk/resources/'
    headers = {
        'Content-Type': 'application/jsin',
        'Authorization': f'OAuth {token_}'
    }
    params = {
        'path': f'disk:/foo_{name}',
        'overwrite': True
    }
    response = requests.put(host, headers=headers, params=params)
    return response

