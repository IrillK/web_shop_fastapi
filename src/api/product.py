from fastapi import APIRouter
from starlette.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT
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


@router.delete("", status_code=HTTP_204_NO_CONTENT)
async def delete_product(product_id: int, uow: UOWDep, user: UserDep):
    await ProductsService().delete_product(uow, product_id)
    return {"status": "Удалено"}
