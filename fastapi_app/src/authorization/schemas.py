from datetime import datetime

from pydantic import BaseModel


class UserDTO(BaseModel):
    id: int
    uuid: str
    first_name: str
    last_name: str
    username: str
    is_verified: bool
    created_at: datetime
    updated_at: datetime

class RequestTokenDTO(BaseModel):
    user_uuid: str

class ResponseTokenDTO(BaseModel):
    access_token: str
    refresh_token: str
    user_id: int
    user_uuid: str