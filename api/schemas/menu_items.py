from typing import Optional
from pydantic import BaseModel
from ..schemas.recipes import Recipe

class MenuItemBase(BaseModel):
    name: str
    price: float
    description: Optional[str] = None

class MenuItemCreate(MenuItemBase):
    pass

class MenuItemUpdate(BaseModel):
    name: Optional[str] = None
    price: Optional[int] = None
    description: Optional[str] = None

class MenuItem(MenuItemBase):
    id: int
    recipe: list[Recipe]

    class Config:
        orm_mode = True