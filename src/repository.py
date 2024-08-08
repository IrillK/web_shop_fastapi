from abc import ABC, abstractmethod

from sqlalchemy import insert, select, update, delete, func
from sqlalchemy.ext.asyncio import AsyncSession


class AbstractRepository(ABC):
    @abstractmethod
    async def add_one():
        raise NotImplementedError
    
    @abstractmethod
    async def add_and_return_one():
        raise NotImplementedError
    
    @abstractmethod
    async def edit_one():
        raise NotImplementedError
    
    @abstractmethod
    async def delete_one():
        raise NotImplementedError
    
    @abstractmethod
    async def find_one():
        raise NotImplementedError
    
    @abstractmethod
    async def find_filter():
        raise NotImplementedError
    
    @abstractmethod
    async def find_all():
        raise NotImplementedError
    
    @abstractmethod
    async def count_all():
        raise NotImplementedError


class SQLAlchemyRepository(AbstractRepository):
    model = None

    def __init__(self, session: AsyncSession):
        self.session = session