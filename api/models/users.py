import enum
from sqlalchemy import Column, ForeignKey, Integer, String, Enum
from sqlalchemy.orm import relationship
from ..dependencies.database import Base

class RoleEnum(enum.Enum):
    CUSTOMER = "customer"
    OWNER = "owner"
    STAFF = "staff"

class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True, autoincrement=True, nullable=False)
    role = Column(Enum(RoleEnum), nullable=False, server_default=RoleEnum.CUSTOMER.value)
    name = Column(String(100))
    username = Column(String(20), nullable=False, unique = True)
    password = Column(String(128), nullable=False)

    reviews = relationship("RatingReview", back_populates="user", uselist=False)