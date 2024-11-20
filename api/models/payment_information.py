from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class Payment_information(Base):
    __tablename__ = "Payment_information"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    cardInformation = Column(String, nullable=False)
    transactionStatus = Column(String, nullable=False)
    paymentType = Column(String, nullable=False)

