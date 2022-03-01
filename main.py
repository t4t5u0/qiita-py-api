import uvicorn
from fastapi import FastAPI


from qiita_py_sdk.getArticle import getArticle, Article


app = FastAPI()


@app.get("/v1/qiita/{user_id}")
async def get_articles(user_id: str) -> list[Article]:
    return getArticle(user_id)


def main():
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)


if __name__ == "__main__":
    main()
