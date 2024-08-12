from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel

from schemas.user import UserSchemaName


class ProductSchemaAdd(BaseModel):
    name: str
    fullname: str = None
    # seller_id: int


class ProductSchemaOut(ProductSchemaAdd):
    id: int
    seller_id: int

    class Config:
        from_attributes = True

class ProductSchemaSellerOut(ProductSchemaAdd):
    id: int
    seller: UserSchemaName

    class Config:
        from_attributes = True
