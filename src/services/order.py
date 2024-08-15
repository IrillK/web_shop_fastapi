from typing import List
from unitofwork import IUnitOfWork
from schemas.order import OrderSchemaOut


class OrderService:

    async def create_order(
        self, uow: IUnitOfWork, list_product_id: List[int], user_id: int
    ):
        async with uow:
            order = await uow.orders.create_order(list_product_id, user_id)
            await uow.commit()
            return OrderSchemaOut(**order)

    async def get_orders(self, uow: IUnitOfWork, limit: int = 10, offset: int = 0):
        async with uow:
            orders = await uow.orders.find_all()
            return [i.__dict__ for i in orders]
