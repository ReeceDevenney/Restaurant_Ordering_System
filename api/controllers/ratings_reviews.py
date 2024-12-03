from sqlalchemy.orm import Session
from sqlalchemy import func
from fastapi import HTTPException, status, Response, Depends
from ..models import ratings_reviews as model
from ..models import orders as order_model
from sqlalchemy.exc import SQLAlchemyError


def create(db: Session, request):
    new_item = model.Rating_Review(
        user_id=request.user_id,
        order_id=request.order_id,
        rating=request.rating,
        review=request.review
    )

    try:
        db.add(new_item)
        db.commit()
        db.refresh(new_item)
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

    return new_item


def read_all(db: Session):
    try:
        result = db.query(model.Rating_Review).all()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return result


def read_one(db: Session, item_id):
    try:
        item = db.query(model.Rating_Review).filter(model.Rating_Review.review_id == item_id).first()
        if not item:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return item


def update(db: Session, item_id, request):
    try:
        item = db.query(model.Rating_Review).filter(model.Rating_Review.review_id == item_id)
        if not item.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
        update_data = request.dict(exclude_unset=True)
        item.update(update_data, synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return item.first()


def delete(db: Session, item_id):
    try:
        item = db.query(model.Rating_Review).filter(model.Rating_Review.review_id == item_id)
        if not item.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
        item.delete(synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

#If the menu item is below a 3-star review it will be flagged
def get_worst_dishes(db: Session, threshold: float = 3.0):
    try:
        dish_stats = (db.query(order_model.Order.menu_item_id,
            func.avg(model.Rating_Review.rating).label("avg_rating"),
            func.count(model.Rating_Review.review_id).label("review_count"))
        .join(model.Rating_Review, order_model.Order.id == model.Rating_Review.order_id)
        .group_by(order_model.Order.menu_item_id)
        .subquery())

        result = (db.query(
            dish_stats.c.menu_item_id,
            dish_stats.c.avg_rating,
            model.Rating_Review.review,
            model.Rating_Review.rating)
        .join(order_model.Order, order_model.Order.menu_item_id == dish_stats.c.menu_item_id)
        .join(model.Rating_Review, model.Rating_Review.order_id == order_model.Order.id)
        .filter(dish_stats.c.avg_rating < threshold)
        .all())

        # Transform the result into a list of dictionaries
        result = [
            { "menu_item_id": row.menu_item_id,
              "avg_rating": row.avg_rating,
              "review": row.review,
              "rating": row.rating
              }
            for row in result ]
        return result
    except Exception as e:
        print(f"Error fetching worst dishes: {e}")
        return []

