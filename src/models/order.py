from datetime import datetime
from typing import List
from database import Base

from sqlalchemy import (
    TIMESTAMP,
    ForeignKey,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.product import Product


class Order(Base):
    __tablename__ = "order"

    id: Mapped[int] = mapped_column(primary_key=True)
    created_at: Mapped[datetime] = mapped_column(TIMESTAMP, default=datetime.utcnow)

    customer_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    customer: Mapped["User"] = relationship(back_populates="orders")

    products: Mapped[List["OrderProduct"]] = relationship(back_populates="order")


class OrderProduct(Base):
    __tablename__ = "order_product"

    order_id: Mapped[int] = mapped_column(ForeignKey("order.id"), primary_key=True)
    product_id: Mapped[int] = mapped_column(ForeignKey("product.id"), primary_key=True)
    product_count: Mapped[int | None] = mapped_column(default=1)

    order: Mapped["Order"] = relationship(back_populates="products")
    product: Mapped["Product"] = relationship(back_populates="orders")
    

