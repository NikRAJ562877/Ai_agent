# main.py
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from agent_core import llm, search  # import from shared file

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ArticleCheckRequest(BaseModel):
    article_text: str

@app.post("/api/check_fake_news")
async def check_fake_news(request: ArticleCheckRequest):
    article = request.article_text
    search_results = search.run(article)

    prompt = f"""
    Given the article: \"{article}\"
    And the search results: \"{search_results}\"
    Determine if the article is genuine or fake news. Provide a clear explanation.
    """
    response = llm.invoke([{"role": "user", "content": prompt}])
    return {"verdict": response.content}
