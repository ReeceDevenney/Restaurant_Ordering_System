from sqlalchemy.orm import Session
from ..models.payment_information import Payment_information
from ..schemas.payment_information import OrderCreate, PaymentInformationUpdate
from datetime import datetime


def process_payment(db: Session, payment_info: OrderCreate):
    new_payment = Payment_information(
        cardNumber=payment_info.cardInformation,
        cardExpirationDate=datetime.now(),  # Mock date; replace if needed
        paymentType=payment_info.paymentType,
        transactionStatus="Pending",
    )
    db.add(new_payment)
    db.commit()
    db.refresh(new_payment)
    return {"detail": "Payment processed successfully", "payment_id": new_payment.id}


def update_payment_status(db: Session, payment_id: int, payment_update: PaymentInformationUpdate):
    payment = db.query(Payment_information).filter(Payment_information.id == payment_id).first()
    if not payment:
        raise HTTPException(status_code=404, detail="Payment not found")

    if payment_update.transactionStatus:
        payment.transactionStatus = payment_update.transactionStatus

    db.commit()
    db.refresh(payment)
    return {"detail": "Payment updated successfully", "payment_id": payment.id}
