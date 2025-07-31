from src.blog.models import ArticleModel
from src.utils.service import BaseCRUDService


class ArticleService(BaseCRUDService):
    pass

article_service = ArticleService(ArticleModel)