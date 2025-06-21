from src.authorization.models import UserModel
from src.utils.service import BaseCRUDService


class UserService(BaseCRUDService):
    pass

user_service = UserService(UserModel)