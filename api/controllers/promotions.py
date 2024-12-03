from sqlalchemy.orm import Session
from ..models.promotions import Promotion
from ..schemas.promotions import PromotionCreate, PromotionUpdate
from datetime import datetime
from fastapi import HTTPException

def create_promotion(db: Session, promotion_data: PromotionCreate):
    new_promotion = Promotion(
        code=promotion_data.code,
        discount=promotion_data.discount,
        isActive=promotion_data.isActive,
        expirationDate=datetime.now(),  # Replace with actual expiration date if needed
    )
    db.add(new_promotion)
    db.commit()
    db.refresh(new_promotion)
    return new_promotion


def get_promotion_by_code(db: Session, code: str):
    return db.query(Promotion).filter(Promotion.code == code).first()


def get_all_promotions(db: Session):
    return db.query(Promotion).all()


def update_promotion(db: Session, code: str, promotion_update: PromotionUpdate):
    promotion = get_promotion_by_code(db, code)
    if not promotion:
        raise HTTPException(status_code=404, detail="Promotion not found")

    for key, value in promotion_update.dict(exclude_unset=True).items():
        setattr(promotion, key, value)

    db.commit()
    db.refresh(promotion)
    return promotion


def delete_promotion(db: Session, code: str):
    promotion = get_promotion_by_code(db, code)
    if not promotion:
        raise HTTPException(status_code=404, detail="Promotion not found")

    db.delete(promotion)
    db.commit()
