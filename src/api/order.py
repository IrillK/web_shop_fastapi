from fastapi import APIRouter
from starlette.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT
from typing import List

from dependencies import UOWDep, UserDep
from services.order import OrderService


router = APIRouter(
    prefix="/orders",
    tags=["Orders"],
)

@router.get("")
async def get_orders(
    uow: UOWDep,
    # user: UserDep,
    limit: int = 10,
    offset: int = 0,
):
    orders = await OrderService().get_orders(uow, limit=limit, offset=offset)
    return orders


@router.post("", status_code=HTTP_201_CREATED)
async def create_order(products_list: List[int], uow: UOWDep, user: UserDep):
    order = await OrderService().create_order(uow, products_list, user.id)
    return {"products_list": products_list, "order": order}


