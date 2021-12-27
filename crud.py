from sqlalchemy.orm import Session

import models
import schemas
from sqlalchemy import func, distinct


def get_items(db: Session):
    return db.query(models.Item).all()


def get_stats(db: Session):
    recordsBySize = db.query(func.count(distinct(models.Item.size))).all()
    recordsByManafacture = db.query(func.count(distinct(models.Item.manufacture))).all()

    return {"manufacturesCount": recordsByManafacture, "sizes": recordsBySize}


def create_item(db: Session, item: schemas.ItemCreate):
    db_item = models.Item(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
