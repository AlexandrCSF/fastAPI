from typing import Optional

from pydantic import BaseModel

class ProductCardRequestDTO(BaseModel):
    id: int

class ProductCardResponseDTO(BaseModel):
    id: int
    name: str
    price: int
    description: Optional[str]
