from repository import SQLAlchemyRepository
from models.product import Product


class ProductRepository(SQLAlchemyRepository):
    model = Product
