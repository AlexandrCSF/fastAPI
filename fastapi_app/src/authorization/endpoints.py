from fastapi import Depends, APIRouter
from sqlalchemy.ext.asyncio import AsyncSession

from db.session import get_db
from src.authorization.schemas import UserDTO, RequestTokenDTO, ResponseTokenDTO
from src.authorization.service import token_service
from src.utils.jwt import get_user

router = APIRouter()

@router.get('/user/',response_model=UserDTO)
async def get_user_data(db: AsyncSession = Depends(get_db), user = Depends(get_user)):
    return user

@router.post('/token/', response_model=ResponseTokenDTO)
async def create_access_token(request_data: RequestTokenDTO, db: AsyncSession = Depends(get_db)):
    token = await token_service.gen_token(db=db, uuid=request_data.user_uuid)
    return token