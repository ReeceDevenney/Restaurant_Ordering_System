from typing import Optional
from pydantic import BaseModel

class ResourceManagementBase(BaseModel):
    item: str
    amount: float

class ResourceManagementCreate(ResourceManagementBase):
    pass

class ResourceManagementUpdate(BaseModel):
    item: Optional[str] = None
    amount: Optional[float] = None

class ResourceManagement(ResourceManagementBase):
    id: int

    class Config:
        orm_mode = True
