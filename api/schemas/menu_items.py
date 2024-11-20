from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL
from sqlalchemy.orm import relationship
from ..dependencies.database import Base


class MenuItem(Base):
    __tablename__ = "menu_items"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, nullable=False, index=True)
    description = Column(String, nullable=True)
    price = Column(DECIMAL, nullable=False, server_default='0.00')
    sandwich_id = Column(Integer, ForeignKey("sandwiches.id"), nullable=True)

    # Relationships
    sandwich = relationship("Sandwich", back_populates="menu_items")