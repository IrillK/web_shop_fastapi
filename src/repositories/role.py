from sqlalchemy import select, func
from auth.models import role
from repository import SQLAlchemyRepository


class RoleRepository(SQLAlchemyRepository):
    model = role

    async def check_role(self, role_id: int, role_name: str):
        stmt = select(func.count(self.model.c.id))\
            .where( ((self.model.columns.id == role_id) and (self.model.name == role_name)) )
        
        res = await self.session.execute(stmt)
        res = res.scalar()
        return res == 1
         