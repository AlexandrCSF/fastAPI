from datetime import datetime
from typing import Optional, List

from pydantic import BaseModel, ConfigDict

from src.authorization.schemas import UserDTO


class ProductCardRequestDTO(BaseModel):
    id: int


class ProductCardDTO(BaseModel):

    id: int
    name: str
    price: int
    description: Optional[str]


class CommentDTO(BaseModel):
    id: int
    text: Optional[str]
    rating: int
    created_at: datetime
    author: UserDTO
    parent_id: Optional[int]
    product: ProductCardDTO
    replies: List["CommentDTO"] = []

class CommentCreateDTO(BaseModel):
    text: Optional[str] = None
    rating: int
    product_id: int
    parent_id: Optional[int] = None