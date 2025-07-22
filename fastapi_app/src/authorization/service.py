from sqlalchemy import select

from src.authorization.models import UserModel
from src.authorization.schemas import CreateUserDTO
from src.utils.service import BaseCRUDService


class UserService(BaseCRUDService):
    pass

class TokenService:
    async def gen_token(self, db, uuid):
        user = await db.execute(select(UserModel).where(UserModel.uuid == uuid))
        user = user.scalar_one_or_none()
        if user is None:
            user = await user_service.create(db,UserModel(uuid=uuid))

token_service = TokenService()
user_service = UserService(UserModel,CreateUserDTO)