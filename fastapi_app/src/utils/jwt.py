import uuid
from datetime import datetime, timezone, timedelta

from fastapi import Depends, HTTPException
from jose import jwt, JWTError
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from core.config import config
from db.session import get_db
from src.authorization.models import UserModel
from src.authorization.schemas import UserDTO
from src.security import oauth2_scheme

class TokenData(BaseModel):
    user_id: int
    iat: int
    exp: int
    token_type: str

async def get_user(db: AsyncSession = Depends(get_db), token: str = Depends(oauth2_scheme)) -> UserDTO:
    from src.authorization.service import user_service
    try:
        payload = jwt.decode(token,config.SECRET_KEY,algorithms=["HS256"])
        data = TokenData(**payload)
    except JWTError:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Could not validate credentials")
    user = await user_service.get(db, id=data.user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user

def is_valid_uuid(uuid_str):
    try:
        uuid_obj = uuid.UUID(uuid_str)
        return str(uuid_obj) == uuid_str
    except ValueError:
        return False

async def create_token(user: UserModel):
    now = datetime.now(timezone.utc)
    iat = int(now.timestamp())
    expire_access = int((now + timedelta(seconds=config.JWTAuthConfig.access_token_lifetime)).timestamp())
    expire_refresh = int((now + timedelta(seconds=config.JWTAuthConfig.refresh_token_lifetime)).timestamp())

    access_payload = {
        "user_id": user.id,
        "iat": iat,
        "exp": expire_access,
        "token_type": "access"
    }

    refresh_payload = {
        "user_id": user.id,
        "iat": iat,
        "exp": expire_refresh,
        "token_type": "refresh"
    }

    access = jwt.encode(access_payload, config.SECRET_KEY, algorithm="HS256")
    refresh = jwt.encode(refresh_payload, config.SECRET_KEY, algorithm="HS256")

    return {
        "access_token": access,
        "refresh_token": refresh,
    }
