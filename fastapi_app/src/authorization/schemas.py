from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, Field, ConfigDict


class UserDTO(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    id: int
    uuid: UUID
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    username: Optional[str] = None
    is_verified: bool
    created_at: datetime
    updated_at: datetime
    refresh_token: Optional[str] = None

class CreateUserDTO(BaseModel):
    uuid: str
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    username: Optional[str] = None
    is_verified: bool = Field(default=True)

class UpdateUserDTO(BaseModel):
    uuid: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    username: Optional[str] = None
    is_verified: bool = Field(default=True)

class RequestTokenDTO(BaseModel):
    user_uuid: str

class ResponseTokenDTO(BaseModel):
    access_token: str
    refresh_token: str
    user_id: int
    user_uuid: str