from fastapi import FastAPI

from webapp.controllers.article import router
from webapp.controllers.info import router as info_router
from webapp.models.article import ArticleModel


def init_app() -> FastAPI:
    app = FastAPI()
    app.include_router(router)
    app.include_router(info_router)

    article_model = ArticleModel()

    app.dependency_overrides[ArticleModel] = lambda: article_model
    return app