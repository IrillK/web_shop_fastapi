from datetime import datetime
from enum import Enum
from typing import List, Optional

from pydantic import BaseModel

from schemas.user import UserSchemaName
from schemas.product import ProductSchemaAdd, ProductSchemaOut

class StatusEnum(Enum):
    EXECUTED = 'EXECUTED'
    PROCESSED = 'PROCESSED'
    ERROR = 'ERROR'


class OrderProductSchemaOut(BaseModel):
    product_count: int
    product_id: int
    # product: ProductSchemaOut

    class Config:
        from_attributes = True
        

class OrderSchemaOut(BaseModel):
    id: int
    created_at: datetime
    status: StatusEnum
    customer_id: int

    products: List[OrderProductSchemaOut]


    class Config:
        from_attributes = True