from typing import Optional
from pydantic import BaseModel
from ..schemas.orders import OrderShort

class RatingReviewBase(BaseModel):
    rating: float
    review: Optional[str] = None
    order_id: int

class RatingReviewCreate(RatingReviewBase):
    user_id: int
    order_id: int

class RatingReviewUpdate(BaseModel):
    rating: Optional[float] = None
    review: Optional[str] = None

class RatingReview(RatingReviewBase):
    review_id: int
    user_id: int
    order: OrderShort

    class Config:
        orm_mode = True