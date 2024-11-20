from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel
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
    order_status: Optional[int] = None


class Order(OrderBase):
    id: int
    order_date: Optional[datetime] = None
    menu_items: List[MenuItem] = None

    class Config:
        from_attributes = True
        arbitrary_types_allowed = True

