import json
from importlib import resources

class ArticleModel:
    def __init__(self, file_path: str = resources.files("webapp.models") / "data.json") -> None:
        self.file_path = file_path
        self.articles = []
        self._load_articles()

    def _load_articles(self) -> None:
        with open(self.file_path, "rb") as file:
            self.articles = json.load(file)

    def _save_articles(self) -> None:
        with open(self.file_path, "w") as file:
            json.dump(self.articles, file, indent=4, ensure_ascii=False)

    def get_articles(self) -> list[dict]:
        return self.articles

    def save_article(self, article: dict) -> int:
        article_id = len(self.articles)
        article["id"] = article_id
        self.articles.append(article)
        self._save_articles()
        return article_id

    def get_article(self, article_id: int) -> dict | None:
        if 0 <= article_id < len(self.articles):
            return self.articles[article_id]
        return None
