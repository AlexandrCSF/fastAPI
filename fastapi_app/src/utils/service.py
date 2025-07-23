from fastapi.encoders import jsonable_encoder
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession


class BaseCRUDService:
    def __init__(self, model, create_schema, update_schema=None):
        self.model = model
        self.create_schema = create_schema
        self.update_schema = update_schema if update_schema else create_schema

    async def get(self, db: AsyncSession, id: int):
        result = await db.execute(select(self.model).where(self.model.id == id))
        return result.scalar_one()

    async def create(self,db: AsyncSession, obj):
        obj_in_data = jsonable_encoder(obj)
        db_obj = self.model(**obj_in_data)
        db.add(db_obj)
        await db.commit()
        await db.refresh(db_obj)
        return db_obj