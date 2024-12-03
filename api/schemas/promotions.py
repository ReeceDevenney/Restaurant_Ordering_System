from datetime import datetime
from typing import Optional
from pydantic import BaseModel



class PromotionBase(BaseModel):
    code: str
    discount: float


class PromotionCreate(PromotionBase):
    isActive: Optional[bool]

class PromotionUpdate(BaseModel):
    code: Optional[str] = None
    discount: Optional[float] = None
    isActive: Optional[bool] = None
    expirationDate: Optional[datetime] = None


class Promotion(PromotionBase):
    isActive: Optional[bool] = True
    expirationDate: Optional[datetime] = None

    class ConfigDict:
        from_attributes = True
