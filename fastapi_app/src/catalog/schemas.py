from datetime import datetime
from typing import Optional, List

from pydantic import BaseModel

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

class CommentCreateDTO(BaseModel):
    text: Optional[str]
    rating: int

class CommentTreeDTO(CommentDTO):
    replies: List["CommentDTO"] = []
