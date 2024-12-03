from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from ..schemas.menu_items import MenuItem



class OrderBase(BaseModel):
    description: Optional[str] = None
    menu_item_id: int
    users_id: int


class OrderCreate(OrderBase):
    pass


class OrderUpdate(BaseModel):
    customer_name: Optional[str] = None
    description: Optional[str] = None
    order_status: Optional[int] = None

class OrderShort(OrderBase):
    id: int
    order_date: datetime

class Order(OrderBase):
    id: int
    order_date: Optional[datetime] = None
    menu_items: MenuItem = None

    class Config:
        from_attributes = True

