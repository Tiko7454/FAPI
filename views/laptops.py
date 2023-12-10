from sqlalchemy.orm import Session

from models.core import Laptop


def get_laptops(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Laptop).order_by(Laptop.id).offset(skip).limit(limit).all()
