from typing import List

from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from db.session import get_db
from src.authorization.schemas import UserDTO
from src.blog.schemas import ArticleDTO
from src.blog.services import article_service
from src.utils.jwt import get_user

router = APIRouter()

@router.get('/articles/',response_model=List[ArticleDTO])
async def get_articles(db: AsyncSession = Depends(get_db), user: UserDTO = Depends(get_user), offset: int = 0, limit: int = 20):
    values = await article_service.get_multi(db=db,offset=offset,limit=limit)
    return values