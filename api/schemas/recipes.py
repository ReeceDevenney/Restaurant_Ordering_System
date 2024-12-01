from typing import Optional
from pydantic import BaseModel
from ..schemas.resource_management import ResourceManagement


class RecipeBase(BaseModel):
    menu_item: int
    ingredient: int
    amount: int


class RecipeCreate(RecipeBase):
    pass


class RecipeUpdate(BaseModel):
    menu_item: Optional[int]
    ingredient: Optional[int]
    amount: int

class Recipe(RecipeBase):
    id: int
    resource_management: ResourceManagement

    class ConfigDict:
        from_attributes = True
