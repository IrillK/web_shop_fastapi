from collections import Counter

from sqlalchemy import insert, select
from sqlalchemy.orm import selectinload, joinedload
from repository import SQLAlchemyRepository
from models.order import Order, OrderProduct
from models.product import Product
from typing import List


class OrderRepository(SQLAlchemyRepository):
    model = Order
    model_order_product = OrderProduct
    model_product = Product

    async def create_order(self, list_product_id: List[int], customer_id: int) -> int:

        if len(list_product_id) == 0:
            raise ValueError("Пустой список покупок")

        order = self.model(customer_id=customer_id, status="PROCESSED")

        counter_products_id = Counter(list_product_id)

        for product_id, count_products in counter_products_id.items():
            order.products.append(
                self.model_order_product(
                    product_count=count_products, product_id=product_id
                )
            )
        self.session.add(order)
        await self.session.commit()
        # здесь попробовать сделать селект запрос с жойном
        return order.__dict__


class OrderProductRepository(SQLAlchemyRepository):
    model = OrderProduct
    model_product = Product
    model_order = Order

    # async def find_all_with_seller(self, limit: int=10, offset: int =0):
    #     stmt = select(self.model)\
    #         .limit(limit).offset(offset)\
    #         .options(
    #             selectinload(self.model.seller)
    #         )
    #     res_products = await self.session.scalars(stmt)
    #     if res_products is None:
    #         return None
    #     return res_products.all()
