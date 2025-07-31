from typing import List

from pydantic import BaseModel

from src.authorization.schemas import UserDTO

class TagDTO(BaseModel):
    id: int
    name: str

class ArticleDTO(BaseModel):
    id: int
    name: str
    text: str
    author: UserDTO
    tags: List[TagDTO]
