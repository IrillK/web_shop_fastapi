from typing import List
from typing import Optional

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base


class Product(Base):
    __tablename__ = "product"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    fullname: Mapped[Optional[str]]

    seller_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    seller: Mapped["User"] = relationship(back_populates="sold_products")