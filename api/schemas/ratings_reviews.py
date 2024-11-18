from typing import Optional
from pydantic import BaseModel


class RatingReviewBase(BaseModel):
    rating: float
    review: Optional[str] = None

class RatingReviewCreate(RatingReviewBase):
    user_id: int

class RatingReviewUpdate(BaseModel):
    rating: Optional[float] = None
    review: Optional[str] = None

class RatingReview(RatingReviewBase):
    review_id: int
    user_id: int

    class Config:
        orm_mode = True