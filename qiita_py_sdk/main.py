import uvicorn
from fastapi import FastAPI

from libs.getArticle import Article, getArticle

app = FastAPI()

@app.get("/v1/qiita/{user_id}")
async def get_articles(user_id: str) -> list[Article]:
    return getArticle(user_id)

def main():
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

if __name__ == "__main__":
    main()