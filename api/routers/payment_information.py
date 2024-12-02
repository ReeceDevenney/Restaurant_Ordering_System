from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from ..schemas.payment_information import OrderCreate, PaymentInformationUpdate
from ..dependencies.database import engine, get_db
from ..controllers.payment_information import (
    process_payment,
    update_payment_status, apply_promotional_code,
)

router = APIRouter()

@router.post("/pay/")
def process_payment_route(payment_info: OrderCreate, db: Session = Depends(get_db)):
    return process_payment(db, payment_info)

@router.post("/apply-code/")
def apply_promotional_code_route(order_id: int, promo_code: str, db: Session = Depends(get_db)):
    return apply_promotional_code(db, order_id, promo_code)


@router.put("/{payment_id}")
def update_payment_status_route(
    payment_id: int,
    payment_update: PaymentInformationUpdate,
    db: Session = Depends(get_db),
):
    return update_payment_status(db, payment_id, payment_update)
