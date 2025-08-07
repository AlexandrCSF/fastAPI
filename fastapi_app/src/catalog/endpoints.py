from typing import List

from fastapi import APIRouter, Depends, Body
from sqlalchemy.ext.asyncio import AsyncSession

from db.session import get_db
from src.authorization.schemas import UserDTO
from src.catalog.schemas import ProductCardDTO, CommentDTO, CommentCreateDTO
from src.catalog.services import product_service, comment_service
from src.utils.jwt import get_user

router = APIRouter(prefix='/products')

@router.get("/product/", response_model=ProductCardDTO)
async def get_product_card(product_id: int, user: UserDTO = Depends(get_user), db: AsyncSession = Depends(get_db)):
    product = await product_service.get(db=db,id=product_id)
    return product

@router.get('/comment/',response_model=List[CommentDTO])
async def get_product_comments(product_id: int, user: UserDTO = Depends(get_user), db: AsyncSession = Depends(get_db)):
    comments = await comment_service.get_comments_for_product(db=db,product_id=product_id)
    return comments

@router.post("/comment/", response_model=CommentDTO)
async def create_comment(comment_data: CommentCreateDTO = Body(...), user: UserDTO = Depends(get_user), db: AsyncSession = Depends(get_db)):
    comment = await comment_service.create_comment(db=db,obj=comment_data, user=user)
    return comment