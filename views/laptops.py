from sqlalchemy.orm import Session

from models import core


def get_laptops(db: Session, skip: int = 0, limit: int = 100):
    return db.query(core.Laptop).offset(skip).limit(limit).all()
