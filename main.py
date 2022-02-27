from email import header
import imp
import json
from unittest import result

import requests


def main() -> dict:
    with open('./secrets.json') as f:
        json_load = json.load(f)
        AUTHOR = json_load['author']
        TOKEN = json_load['token']

    headers = {'Authorization': 'Bearer ' + TOKEN}

    URL = f'https://qiita.com/api/v2/users/{AUTHOR}/items'

    r_get = requests.get(URL, headers=headers)

    result = [
        {
            'title': item['title'],
            'tags': [{'name': i['tags']} for i in item['tags']],
            'url': item['url'],
        }
        for item in r_get.json()
    ]

    return result

if __name__ == '__main__':
    r = main()

    from pprint import pprint
    pprint(r)