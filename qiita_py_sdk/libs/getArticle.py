
import json
from pydantic import BaseModel

import requests
from fastapi import HTTPException

from pathlib import Path


class Article(BaseModel):
    title: str
    tags: list[dict[str, str]]
    url: str
    likes_count: int
    created_at: str


def getArticle(user_id: str) -> list[Article]:
    p = Path(__file__).resolve().parents[2] / 'secrets.json'
    print(p)
    with open(p ) as f:
        json_load = json.load(f)
        TOKEN = json_load['token']

    headers = {'Authorization': 'Bearer ' + TOKEN}

    URL = f'https://qiita.com/api/v2/users/{user_id}/items'

    # try:
    #     r_get = requests.get(URL, headers=headers)
    # except requests.exceptions.RequestException as e:
    #     raise HTTPException(status_code=404, detail=e)

    r_get = requests.get(URL, headers=headers)

    if r_get.status_code == 404:
        raise HTTPException(status_code=404, detail="user not found")

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
