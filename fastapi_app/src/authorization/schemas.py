from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, Field


class UserDTO(BaseModel):
    id: int
    uuid: UUID
    first_name: str = Field(default=None)
    last_name: str = Field(default=None)
    username: str = Field(default=None)
    is_verified: bool
    created_at: datetime
    updated_at: datetime

class CreateUserDTO(BaseModel):
    uuid: str
    first_name: str
    last_name: str
    username: str
    is_verified: bool = Field(default=True)

class RequestTokenDTO(BaseModel):
    user_uuid: str

class ResponseTokenDTO(BaseModel):
    access_token: str
    refresh_token: str
    user_id: int
    user_uuid: str