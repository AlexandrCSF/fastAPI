from typing import List

from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from sqlalchemy import select, and_
from sqlalchemy.exc import NoResultFound, MultipleResultsFound
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload, selectinload

from src.authorization.models import UserModel
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


class CommentService(BaseCRUDService[CommentModel, CommentCreateDTO, CommentCreateDTO]):
    async def get_comments_for_product(self, db: AsyncSession, *, product_id: int) -> List[CommentModel]:
        comments = await db.execute(select(self.model)
        .where(self.model.product_id == product_id)
        .options(
            selectinload(CommentModel.author),
            selectinload(CommentModel.product),
            selectinload(CommentModel.replies)
        ))

        return comments.unique().scalars().all()

    async def create_comment(self, db: AsyncSession, *, obj: CommentCreateDTO, user: UserModel) -> CommentModel:
        obj_in_data = jsonable_encoder(obj)
        db_obj = self.model(**obj_in_data)
        db_obj.author = user
        db.add(db_obj)
        await db.commit()
        await db.refresh(db_obj)
        return db_obj


comment_service = CommentService(CommentModel)
product_service = BaseCRUDService(ProductModel)
