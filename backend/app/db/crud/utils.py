from app.db.session import Base
from fastapi.exceptions import HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session


def get_all_items(db: Session, model: Base, skip: int = 0, limit: int = 100):
    return db.query(model).offset(offset=skip).limit(limit).all()


def get_item(db: Session, model: Base, _id: int):
    item = db.query(model).filter(model.id == _id).first()
    if not item:
        raise HTTPException(
            status_code=404,
            detail=f"id={_id} is not found in {model.__tablename__}",
        )
    return item


def get_item_by_name(db: Session, model: Base, name: str):
    return db.query(model).first(model.name == name)


def create_item(db: Session, model: Base, payload: BaseModel):
    db_item = model(**payload.dict())
    db.add(db_item)
    db.commit()
    return db_item


def update_item(db: Session, model: Base, _id: int, payload: BaseModel):
    db_item = get_item(db, model, _id)
    update_data = payload.dict(exclude_unset=True)
    for k, v in update_data.items():
        setattr(db_item, k, v)
    db.commit()
    return db_item


def delete_item(db: Session, model: Base, _id: int):
    db_item = get_item(db, model, _id)
    db.delete(db_item)
    db.commit()
    return db_item
