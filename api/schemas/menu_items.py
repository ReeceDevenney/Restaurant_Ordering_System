from typing import Optional
from pydantic import BaseModel

class MenuItemBase(BaseModel):
    name: str
    price: float
    description: Optional[str] = None

class MenuItemCreate(MenuItemBase):
    pass

class MenuItemUpdate(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
    description: Optional[str] = None

class MenuItem(MenuItemBase):
    id: int
    sandwich_id: Optional[int] = None

    class Config:
        orm_mode = True