from sqlalchemy import select
from sqlalchemy.orm import selectinload, joinedload
from repository import SQLAlchemyRepository
from models.product import Product


class ProductRepository(SQLAlchemyRepository):
    model = Product

    async def find_all_with_seller(self, limit: int=10, offset: int =0):
        stmt = select(self.model)\
            .limit(limit).offset(offset)\
            .options(
                selectinload(self.model.seller)
            )
        res_products = await self.session.scalars(stmt)
        if res_products is None:
            return None
        return res_products.all()