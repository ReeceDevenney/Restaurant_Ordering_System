from typing import Optional
from pydantic import BaseModel
from .ratings_reviews import RatingReview

class UserBase(BaseModel):
    name: Optional[str] = None
    username: str
    role: str

class UserCreate(UserBase):
    password: str

class UserUpdate(BaseModel):
    name: Optional[str] = None
    username: Optional[str] = None
    role: Optional[str] = None

class User(UserBase):
    user_id: int
    reviews: RatingReview

    class Config:
        orm_mode = True