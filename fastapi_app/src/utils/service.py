from typing import TypeVar, Generic, Type, Optional

from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from sqlalchemy import select
from sqlalchemy.event import remove
from sqlalchemy.exc import NoResultFound
from sqlalchemy.ext.asyncio import AsyncSession

from db.base_class import Base

ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class BaseCRUDService(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: Type[ModelType]):
        self.model = model

    async def get(self, db: AsyncSession, *, id: int) -> Optional[ModelType]:
        elem = await db.execute(select(self.model).where(self.model.id == id))
        return elem.scalar_one()

    async def create(self, db: AsyncSession, *, obj: CreateSchemaType) -> ModelType:
        obj_in_data = jsonable_encoder(obj)
        db_obj = self.model(**obj_in_data)
        db.add(db_obj)
        await db.commit()
        await db.refresh(db_obj)
        return db_obj

    async def edit(self, db: AsyncSession, *, obj: ModelType, edit_fields: UpdateSchemaType) -> ModelType:
        obj_data = jsonable_encoder(obj)
        update_data = edit_fields.model_dump(mode='json',exclude_unset=True,exclude_none=True)
        for field in obj_data:
            if field in update_data:
                setattr(obj, field, update_data[field])
        db.add(obj)
        await db.commit()
        await db.refresh(obj)
        return obj

    async def remove(self, db: AsyncSession, *, id: int) -> ModelType:
        elem = await db.execute(select(self.model).where(self.model.id == id))
        if not elem:
            raise NoResultFound(f'No such record with id: {id}')
        await db.delete(elem)
        await db.commit()
        return elem