from fastapi import APIRouter
from starlette.status import HTTP_201_CREATED
from typing import List

from dependencies import UOWDep, UserDep
from schemas.product import ProductSchemaAdd, ProductSchemaOut
from services.product import ProductsService

router = APIRouter(
    prefix="/products",
    tags=["Products"],
)


@router.get("")
async def get_products(
    uow: UOWDep,
    # user: UserDep,
    limit: int = 10,
    offset: int = 0,
):
    products = await ProductsService().get_products(uow, limit=limit, offset=offset)
    return products


@router.post("", status_code=HTTP_201_CREATED)
async def create_product(product: ProductSchemaAdd, uow: UOWDep, user: UserDep):
    product_id = await ProductsService().add_product(uow, product, user.id)
    return {"product_id": product_id}
