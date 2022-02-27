import json

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
            'tags': [{'name': i['name']} for i in item['tags']],
            'url': item['url'],
            'likes_count': item['likes_count'],
            'created_at': item['created_at'],
        }
        for item in r_get.json()
    ]

    return result


if __name__ == '__main__':
    main()
