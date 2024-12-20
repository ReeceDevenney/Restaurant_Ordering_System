from datetime import datetime
from typing import Optional
from pydantic import BaseModel



class PaymentInformationBase(BaseModel):
    cardNumber: str
    cardExpiration: datetime
    paymentType: str
    transactionStatus: str


class OrderCreate(PaymentInformationBase):
    pass


class PaymentInformationUpdate(BaseModel):
    transactionStatus: Optional[str] = None


class PaymentInformation(PaymentInformationBase):
    id: int

    class ConfigDict:
        from_attributes = True
