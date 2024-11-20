from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base

class Resource_management(Base):
    __tablename__ = 'resource_management'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    item = Column(String(20), index=True, nullable=False)
    amount = Column(Integer, index=True, nullable=False, server_default='0')

    recipes = relationship('Recipe', backref='resource')
