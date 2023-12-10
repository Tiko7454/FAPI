from sqlalchemy.orm import Session

from models.core import Laptop


def get_laptops(db: Session, skip: int, limit: int):
    return db.query(Laptop).order_by(Laptop.id).offset(skip).limit(limit).all()
