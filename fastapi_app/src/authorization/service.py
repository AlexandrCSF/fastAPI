from fastapi import HTTPException
from sqlalchemy import select

from src.authorization.models import UserModel
from src.authorization.schemas import ResponseTokenDTO
from src.utils.jwt import create_token, is_valid_uuid
from src.utils.service import BaseCRUDService

class TokenService:
    async def gen_token(self, db, *, uuid):
        if not is_valid_uuid(uuid):
            raise HTTPException(status_code=401,detail="Input valid UUID")
        user = await db.execute(select(UserModel).where(UserModel.uuid == uuid))
        user = user.scalar_one_or_none()
        if user is None:
            user = await user_service.create(db, obj=UserModel(uuid=uuid))
        token = await create_token(user)
        user.refresh_token = token['refresh_token']
        db.add(user)
        await db.commit()
        await db.refresh(user)
        return ResponseTokenDTO(
            access_token=token['access_token'],
            refresh_token=token['refresh_token'],
            user_id=user.id,
            user_uuid=str(user.uuid)
        )

token_service = TokenService()
user_service = BaseCRUDService(UserModel)