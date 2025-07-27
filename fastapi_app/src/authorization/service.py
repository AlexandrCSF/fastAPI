from sqlalchemy import select

from src.authorization.models import UserModel
from src.authorization.schemas import ResponseTokenDTO
from src.utils.jwt import create_token
from src.utils.service import BaseCRUDService

class TokenService:
    async def gen_token(self, db, uuid):
        user = await db.execute(select(UserModel).where(UserModel.uuid == uuid))
        user = user.scalar_one_or_none()
        if user is None:
            user = await user_service.create(db, obj=UserModel(uuid=uuid))
        token = await create_token(user)
        return ResponseTokenDTO(
            access_token=token['access_token'],
            refresh_token=token['refresh_token'],
            user_id=user.id,
            user_uuid=str(user.uuid)
        )

token_service = TokenService()
user_service = BaseCRUDService(UserModel)