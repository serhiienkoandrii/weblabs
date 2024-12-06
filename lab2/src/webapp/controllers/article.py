from typing import Annotated

from fastapi import APIRouter, Request
from fastapi.params import Depends, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from importlib import resources

from webapp.models.article import ArticleModel

templates = Jinja2Templates(directory=resources.files("webapp.views"))
router = APIRouter(prefix="/articles")


@router.get("/")
async def get_articles(
    request: Request,
    articles_reader: Annotated[ArticleModel, Depends(ArticleModel)]
):
    articles = articles_reader.get_articles()
    return templates.TemplateResponse("index.html", {"request": request, "articles": articles})


@router.get("/items/{article_id}")
async def get_article(
    request: Request,
    article_reader: Annotated[ArticleModel, Depends(ArticleModel)],
    article_id: int
):
    article = article_reader.get_article(article_id)
    return templates.TemplateResponse("article.html", {"request": request, "article": article})


@router.post("/")
async def post_article(
    article_writer: Annotated[ArticleModel, Depends(ArticleModel)],
    title: str = Form(...),
    preview: str = Form(...),
    content: str = Form(...)
):
    article_id = article_writer.save_article({"title": title, "preview": preview, "content": content})
    new_article_html = f"""
    <div 
        class="article-preview" 
        hx-get="items/{article_id}" 
        hx-trigger="click"
        hx-target="#main-content"
    >
        <h2>{title}</h2>
        <p>{preview}</p>
    </div>
    """
    return HTMLResponse(new_article_html)