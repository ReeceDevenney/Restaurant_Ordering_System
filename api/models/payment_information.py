from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class Payment_information(Base):
    __tablename__ = "Payment_information"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    cardNumber = Column(String(20))
    cardExpirationDate = Column(DATETIME)
    transactionStatus = Column(String(15), nullable = False)
    paymentType = Column(String(10), nullable=False)

