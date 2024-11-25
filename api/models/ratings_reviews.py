from enum import unique

from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, CheckConstraint
from sqlalchemy.orm import relationship
from ..dependencies.database import Base


class Rating_Review(Base):
    __tablename__ = "ratings_reviews"

    review_id = Column(Integer, primary_key=True, index = True, autoincrement=True, nullable=False)
    user_id = Column(Integer, ForeignKey("users.user_id"), nullable=False, unique=True)
    order_id = Column(Integer, ForeignKey("orders.order_id"), nullable=False, unique=True)
    reviewer_name = Column(String(100))
    rating = Column(DECIMAL(precision=2, scale=1), nullable=False)
    review = Column(String(300))


    user = relationship("User", back_populates="reviews")
    order = relationship("Order", back_populates="reviews")

    __table_args__ = (
        CheckConstraint('rating >= 0 AND rating <= 5', name='check_rating_range'),
    )
