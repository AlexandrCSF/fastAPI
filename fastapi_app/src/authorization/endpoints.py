from fastapi import Depends, APIRouter
from src.authorization.schemas import UserDTO
from src.utils.jwt import get_user

router = APIRouter()

@router.get('/user/')
def get_user_data(user: UserDTO=Depends(get_user)):
    pass

@router.post('/token/')
def create_access_token():
    pass