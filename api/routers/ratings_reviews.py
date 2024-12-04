from fastapi import APIRouter, Depends, FastAPI, status, Response
from sqlalchemy.orm import Session
from ..controllers import ratings_reviews as controller
from ..schemas import ratings_reviews as schema
from ..dependencies.database import engine, get_db

router = APIRouter(
    tags=['Ratings_Reviews'],
    prefix="/ratings_reviews"
)


@router.post("/", response_model=schema.RatingReview)
def create(request: schema.RatingReviewCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, request=request)


@router.get("/", response_model=list[schema.RatingReview])
def read_all(db: Session = Depends(get_db)):
    return controller.read_all(db)

@router.get("/bad/{threshold}")
def get_worst_dishes(threshold: float = 3.0, db: Session = Depends(get_db)):
    return controller.get_worst_dishes(db, threshold)

@router.get("/{review_id}", response_model=schema.RatingReview)
def read_one(review_id: int, db: Session = Depends(get_db)):
    return controller.read_one(db, item_id=review_id)


@router.put("/{review_id}", response_model=schema.RatingReview)
def update(review_id: int, request: schema.RatingReviewUpdate, db: Session = Depends(get_db)):
    return controller.update(db=db, request=request, item_id=review_id)


@router.delete("/{review_id}")
def delete(review_id: int, db: Session = Depends(get_db)):
    return controller.delete(db=db, item_id=review_id)




