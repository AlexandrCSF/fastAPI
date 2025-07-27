from fastapi import APIRouter, Depends, Body
from sqlalchemy.ext.asyncio import AsyncSession

from db.session import get_db
from src.authorization.schemas import UserDTO
from src.catalog.schemas import ProductCardRequestDTO, ProductCardResponseDTO
from src.catalog.services import product_service
from src.utils.jwt import get_user

router = APIRouter()

@router.get("/product/",response_model=ProductCardResponseDTO)
async def get_product_card(product_id: int, user: UserDTO = Depends(get_user), db: AsyncSession = Depends(get_db)):
    product = await product_service.get(db=db,id=product_id)
    return product