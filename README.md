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

