from sqlalchemy.orm import Session
from fastapi import HTTPException
from ..models.payment_information import Payment_information
from ..models.promotions import Promotion
from ..models.orders import Order
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

def apply_promotional_code(db: Session, order_id: int, promo_code: str):
    # Fetch the order
    order = db.query(Order).filter(Order.id == order_id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")

    # Fetch the promotion
    promotion = db.query(Promotion).filter(Promotion.code == promo_code).first()
    if not promotion:
        raise HTTPException(status_code=404, detail="Promotion code not found")

    # Check if the promotion is active and not expired
    if not promotion.isActive:
        raise HTTPException(status_code=400, detail="Promotion code is inactive")
    if promotion.expirationDate < datetime.now():
        raise HTTPException(status_code=400, detail="Promotion code has expired")

    # Apply the discount
    discount_amount = (float(promotion.discount) / 100) * order.total_price
    order.total_price -= discount_amount
    db.commit()

    return {
        "detail": "Promotion applied successfully",
        "discount_amount": round(discount_amount, 2),
        "new_total": round(order.total_price, 2),
    }


def update_payment_status(db: Session, payment_id: int, payment_update: PaymentInformationUpdate):
    payment = db.query(Payment_information).filter(Payment_information.id == payment_id).first()
    if not payment:
        raise HTTPException(status_code=404, detail="Payment not found")

    if payment_update.transactionStatus:
        payment.transactionStatus = payment_update.transactionStatus

    db.commit()
    db.refresh(payment)
    return {"detail": "Payment updated successfully", "payment_id": payment.id}
