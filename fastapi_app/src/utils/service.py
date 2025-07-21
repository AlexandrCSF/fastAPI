from fastapi.encoders import jsonable_encoder
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession


class BaseCRUDService:
    def __init__(self, model, create_schema, update_schema):
        self.model = model
        self.create_schema = create_schema
        self.update_schema = update_schema

    async def get(self,db: AsyncSession, id: int):
        result = await db.execute(select(self.model).where(self.model.id == id))
        return result.scalar_one()
    #TODO: Дописать
    async def create(self,db: AsyncSession, obj):
        return
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)
        db_session.add(db_obj)
        db_session.commit()
        db_session.refresh(db_obj)
        return db_obj