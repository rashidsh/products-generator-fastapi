from fastapi import APIRouter, Depends

from app.auth import get_current_user
from app.crud import products_crud, users_crud
from app.models import User, User_Pydantic, UserIn_Pydantic
from app.schemas.base import page_params, Page
from app.schemas.products import ProductSchema

router = APIRouter()


@router.get('/products', response_model=Page[ProductSchema])
async def get_products(params: dict = Depends(page_params), user: User = Depends(get_current_user)):
    items, total = products_crud.get_all(**params)
    return Page.create(items, params, total=total)


@router.get('/users', response_model=list[User_Pydantic])
async def get_users(user: User = Depends(get_current_user)):
    return await User_Pydantic.from_queryset(User.all())


@router.post('/users', response_model=User_Pydantic)
async def create_user(data: UserIn_Pydantic, user: User = Depends(get_current_user)):
    user = await users_crud.create_user(data.dict(exclude_unset=True))
    return await User_Pydantic.from_tortoise_orm(user)
