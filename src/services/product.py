from unitofwork import IUnitOfWork

from schemas.product import ProductSchemaAdd, ProductSchemaOut, ProductSchemaSellerOut


class ProductsService:

    async def get_products(self, uow: IUnitOfWork, limit: int = 10, offset: int = 0):
        async with uow:
            products = await uow.products.find_all_with_seller(
                limit=limit, offset=offset
            )
            return [ProductSchemaSellerOut(**i.__dict__) for i in products]

    async def add_product(
        self,
        uow: IUnitOfWork,
        product: ProductSchemaAdd,
        user_id: int,
    ):
        product_dict = product.model_dump()
        product_dict["seller_id"] = user_id
        async with uow:
            product_id = await uow.products.add_one(product_dict)
            await uow.commit()
            return product_id

    async def delete_product(self, uow: IUnitOfWork, product_id: int):
        async with uow:
            await uow.products.delete_one(product_id)
            await uow.commit()
