from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL
from sqlalchemy.orm import relationship
from ..dependencies.database import Base


class MenuItem(Base):
    __tablename__ = "menu_items"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    description = Column(String(100), nullable=True)
    price = Column(DECIMAL(4, 2), nullable=False, default=0.0)

    # Relationships

    order = relationship("Orders", back_populates="menu_items")