from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base

class Recipe(Base):
    __tablename__ = 'recipes'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    menu_item = Column(Integer, ForeignKey("menu_items.id"),index=True, nullable=False)
    ingredient = Column(Integer, ForeignKey("resource_management.id"),index=True, nullable=False)
    amount = Column(Integer, index=True, nullable=False, server_default='0')

    menu_items = relationship("MenuItem", back_populates="recipes")
    resource_management = relationship("Resource_management", back_populates="recipes")