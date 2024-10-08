from abc import ABC, abstractmethod
from typing import Type

from database import async_session_maker

from repositories.user import UserRepository
from repositories.product import ProductRepository
from repositories.role import RoleRepository
from repositories.order import OrderRepository, OrderProductRepository


# https://github1s.com/cosmicpython/code/tree/chapter_06_uow
class IUnitOfWork(ABC):
    users: Type[UserRepository]
    products: Type[ProductRepository]
    orders: Type[OrderRepository]
    orders_products: Type[OrderProductRepository]
    role: Type[RoleRepository]

    @abstractmethod
    def __init__(self): ...

    @abstractmethod
    async def __aenter__(self): ...

    @abstractmethod
    async def __aexit__(self, *args): ...

    @abstractmethod
    async def commit(self): ...

    @abstractmethod
    async def rollback(self): ...


class UnitOfWork:
    def __init__(self):
        self.session_factory = async_session_maker

    async def __aenter__(self):
        self.session = self.session_factory()

        self.users = UserRepository(self.session)
        self.products = ProductRepository(self.session)
        self.orders = OrderRepository(self.session)
        self.orders_products = OrderProductRepository(self.session)
        self.role = RoleRepository(self.session)

    async def __aexit__(self, *args):
        await self.rollback()
        await self.session.close()

    async def commit(self):
        await self.session.commit()

    async def rollback(self):
        await self.session.rollback()
