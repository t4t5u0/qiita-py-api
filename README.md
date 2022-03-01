# qiita-py-api

Qiitaのあるユーザーの記事を一括で取得するWeb APIサーバーです．Qiita API のラッパーです．

## usage

secrets.jsonにQiita APIのシークレットを書き込みます．

```sh
poetry install
poetry run start
```

```sh
curl -X 'GET' \
  'http://127.0.0.1:8000/v1/qiita/t4t5u0' \
  -H 'accept: application/json'
```

result 

```json
[
  {
    "title": "unzip が文字化けしてる (-O オプションがない, Arch Linux)",
    "tags": [
      {
        "name": "arch"
      },
      {
        "name": "unzip"
      }
    ],
    "url": "https://qiita.com/t4t5u0/items/bec6de32b45d6996c277",
    "likes_count": 0,
    "created_at": "2021-01-06T18:48:46+09:00"
  },
  {
    "title": "PythonでJSONファイルを作成する方法",
    "tags": [
      {
        "name": "Python"
      },
      {
        "name": "JSON"
      },
      {
        "name": "Python3"
      }
    ],
    "url": "https://qiita.com/t4t5u0/items/530d3eb7453aa8ad8abf",
    "likes_count": 6,
    "created_at": "2020-06-08T02:45:25+09:00"
  },
  {
    "title": "discord.py で 質問箱Bot を作った話",
    "tags": [
      {
        "name": "Python"
      },
      {
        "name": "Python3"
      },
      {
        "name": "discord"
      }
    ],
    "url": "https://qiita.com/t4t5u0/items/efa6d83fc83dc3703935",
    "likes_count": 1,
    "created_at": "2020-05-09T18:36:53+09:00"
  }
]
```