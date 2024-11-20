import enum

from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME, Enum
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class OrderStatusEnum(enum.Enum):
    RECEIVED = "Received"
    IN_PROGRESS = "In Progress"
    DELIVERED = "Delivered"


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    customer_name = Column(String(100))
    order_date = Column(DATETIME,  server_default=str(datetime.now()))
    description = Column(String(300))
    order_status = Column(Enum(OrderStatusEnum), server_default=OrderStatusEnum.RECEIVED.value)
    menu_item_id = Column(Integer, ForeignKey("menu_items.id"))

    menu_items = relationship("MenuItem", back_populates="orders")
