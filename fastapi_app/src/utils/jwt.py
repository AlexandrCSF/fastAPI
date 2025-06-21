from fastapi import Depends, HTTPException
from jose import jwt, JWTError
from pydantic import BaseModel
from starlette import status

from core.config import config
from src.authorization.schemas import UserDTO
from src.authorization.service import user_service
from src.security import oauth2_scheme


class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: int

def get_user_from_db(user_id):
    return user_service.get(user_id)

def get_user(token: str = Depends(oauth2_scheme)) -> UserDTO:
    try:
        payload = jwt.decode(token,config.SECRET_KEY,algorithms=["HS256"])
        data = TokenData(**payload)
    except JWTError:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Could not validate credentials")
    user = get_user_from_db(data.id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
