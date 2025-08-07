from typing import List

from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.exc import NoResultFound, MultipleResultsFound
from sqlalchemy.ext.asyncio import AsyncSession

from src.catalog.models import ProductModel, CommentModel
from src.catalog.schemas import CommentCreateDTO
from src.utils.service import BaseCRUDService


class ProductService:
    async def get(self, db: AsyncSession, *, id: int) -> ProductModel:
        elem = await db.execute(select(self.model).where(self.model.id == id))
        try:
            return elem.scalar_one()
        except NoResultFound:
            raise HTTPException(
                status_code=404,
                detail=f"Record with id {id} not found"
            )
        except MultipleResultsFound:
            raise HTTPException(
                status_code=401,
                detail=f"Multiple results found"
            )

class CommentService(BaseCRUDService[CommentModel,CommentCreateDTO,CommentCreateDTO]):
    async def get_comments_for_product(self, db: AsyncSession, *, product_id: int) -> List[CommentModel]:
        elem = await db.execute(select(self.model).where(self.model.product_id == product_id))
        return elem.scalars()

comment_service = CommentService(CommentModel)
product_service = BaseCRUDService(ProductModel)