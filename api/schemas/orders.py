from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from .order_details import OrderDetail
from ..models.menu_items import MenuItem


class OrderBase(BaseModel):
    customer_name: str
    description: Optional[str] = None
    amount: float
    menu_item_id: int


class OrderCreate(OrderBase):
    pass


class OrderUpdate(BaseModel):
    customer_name: Optional[str] = None
    description: Optional[str] = None


class Order(OrderBase):
    id: int
    order_date: Optional[datetime] = None
    menu_item: MenuItem = None

    class ConfigDict:
        from_attributes = True
