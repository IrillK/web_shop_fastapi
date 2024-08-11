from abc import ABC, abstractmethod

from sqlalchemy import insert, select, update, delete, func
from sqlalchemy.ext.asyncio import AsyncSession


class AbstractRepository(ABC):
    @abstractmethod
    async def add_one():
        raise NotImplementedError
    
    # @abstractmethod
    # async def add_and_return_one():
    #     raise NotImplementedError
    
    # @abstractmethod
    # async def edit_one():
    #     raise NotImplementedError
    
    # @abstractmethod
    # async def delete_one():
    #     raise NotImplementedError
    
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
    
    async def find_one(self, **filter_by):
        stmt = select(self.model).filter_by(**filter_by)
        res = await self.session.execute(stmt)
        res = res.scalar_one_or_none()
        if res is None:
            return None
        return res

    async def find_filter(self, **filter_by):
        stmt = select(self.model).filter_by(**filter_by)
        res = await self.session.execute(stmt)
        return res.all()

    async def find_all(self, limit: int=10, offset: int =0):
        stmt = select(self.model)\
            .limit(limit).offset(offset)
        res = await self.session.scalars(stmt)
        return res.all()
        
    async def count_all(self):
        stmt = select(func.count(self.model.id))
        res = await self.session.execute(stmt)
        res = res.scalar()
        return res

    async def add_one(self, data: dict) -> int:
        stmt = insert(self.model).values(**data).returning(self.model.id)
        res = await self.session.execute(stmt)
        return res.scalar_one()