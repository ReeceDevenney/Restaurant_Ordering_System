from typing import Optional
from pydantic import BaseModel

class MenuItemBase(BaseModel):
    name: str
    price: int
    description: Optional[str] = None

class MenuItemCreate(MenuItemBase):
    pass

class MenuItemUpdate(BaseModel):
    name: Optional[str] = None
    price: Optional[int] = None
    description: Optional[str] = None

class MenuItem(MenuItemBase):
    id: int

    class Config:
        orm_mode = True
        arbitrary_types_allowed=True