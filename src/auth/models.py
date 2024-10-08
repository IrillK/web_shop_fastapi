from datetime import datetime
from typing import List

from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import (
    Table,
    Column,
    Integer,
    String,
    TIMESTAMP,
    ForeignKey,
    JSON,
    Boolean,
    MetaData,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base, metadata
from models.order import Order
from models.product import Product

from auth.schemas import UserNameSchema

role = Table(
    "role",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("permissions", JSON),
)


class User(SQLAlchemyBaseUserTable[int], Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False)
    username = Column(String, nullable=False)
    registered_at = Column(TIMESTAMP, default=datetime.utcnow)
    role_id = Column(Integer, ForeignKey(role.c.id))
    hashed_password: str = Column(String(length=1024), nullable=False)
    is_active: bool = Column(Boolean, default=True, nullable=False)
    is_superuser: bool = Column(Boolean, default=False, nullable=False)
    is_verified: bool = Column(Boolean, default=False, nullable=False)

    sold_products: Mapped[List["Product"]] = relationship(back_populates="seller")
    orders: Mapped[List["Order"]] = relationship(back_populates="customer")

    def to_short_read_model(self) -> UserNameSchema:
        return UserNameSchema(
            id=self.id,
            username=self.username,
        )
