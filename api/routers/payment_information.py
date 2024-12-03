from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from ..schemas.payment_information import OrderCreate, PaymentInformationUpdate
from ..dependencies.database import engine, get_db
from ..controllers.payment_information import (
    process_payment,
    update_payment_status,
    get_payment,
    get_all_payments,
    delete_payment,
    apply_promotional_code
)

router = APIRouter(
    tags=['Payments'],
    prefix="/payments"
)


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

@router.get("/{payment_id}")
def get_payment_route(payment_id: int, db: Session = Depends(get_db)):
    payment = get_payment(db, payment_id)
    if not payment:
        raise HTTPException(status_code=404, detail="Payment not found")
    return payment

@router.get("/")
def get_all_payments_route(db: Session = Depends(get_db)):
    return get_all_payments(db)

@router.delete("/{payment_id}")
def delete_payment_route(payment_id: int, db: Session = Depends(get_db)):
    delete_payment(db, payment_id)
    return {"detail": f"Payment with ID {payment_id} deleted successfully"}
