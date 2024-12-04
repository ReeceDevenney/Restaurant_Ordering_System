from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from ..models import orders as model
from ..schemas.resource_management import ResourceAmount
from sqlalchemy.exc import SQLAlchemyError
from ..controllers.menu_items import read_one as getMenuItem
from ..controllers.resource_management import update as updateResource



def create(db: Session, request):
    new_item = model.Order(
        description=request.description,
        menu_item_id=request.menu_item_id,
        users_id=request.users_id
    )
    menuItems = getMenuItem(db, new_item.menu_item_id)
    print("Testing")
    idArr = []
    ammArr = []
    for item in menuItems.recipes:
        if item.amount > item.resource_management.amount:
            err = "not enough " + item.resource_management.item + " to complete order"
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=err)
        idArr.append(item.resource_management.id)
        ammArr.append(item.resource_management.amount - item.amount)
    i = 0
    for id in idArr:
        test = ResourceAmount(amount=ammArr[i])
        updateResource(db, id, test)
        i = i + 1

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
        result = db.query(model.Order).all()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return result

def read_by_date_range(db: Session, start_date, end_date):
    try:
        item = db.query(model.Order).filter(model.Order.order_date >= start_date, model.Order.order_date <= end_date).all()
        if not item:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Description not found!")
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return item

def read_one(db: Session, item_id):
    try:
        item = db.query(model.Order).filter(model.Order.id == item_id).first()
        if not item:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return item


def update(db: Session, item_id, request):
    try:
        item = db.query(model.Order).filter(model.Order.id == item_id)
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
        item = db.query(model.Order).filter(model.Order.id == item_id)
        if not item.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
        item.delete(synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
