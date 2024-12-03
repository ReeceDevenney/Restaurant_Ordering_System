from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from ..schemas.promotions import PromotionCreate, PromotionUpdate
from ..dependencies.database import engine, get_db
from ..controllers.promotions import (
    create_promotion,
    get_promotion_by_code,
    get_all_promotions,
    update_promotion,
    delete_promotion,
)

router = APIRouter(
    tags=["promotions"],
    prefix="/promotions"
)

@router.post("/")
def create_promotion_route(promotion: PromotionCreate, db: Session = Depends(get_db)):
    return create_promotion(db, promotion)

@router.get("/{code}")
def get_promotion_route(code: str, db: Session = Depends(get_db)):
    promotion = get_promotion_by_code(db, code)
    if not promotion:
        raise HTTPException(status_code=404, detail="Promotion not found")
    return promotion

@router.get("/")
def get_all_promotions_route(db: Session = Depends(get_db)):
    return get_all_promotions(db)

@router.put("/{code}")
def update_promotion_route(code: str, promotion_update: PromotionUpdate, db: Session = Depends(get_db)):
    return update_promotion(db, code, promotion_update)

@router.delete("/{code}")
def delete_promotion_route(code: str, db: Session = Depends(get_db)):
    delete_promotion(db, code)
    return {"detail": "Promotion deleted successfully"}
