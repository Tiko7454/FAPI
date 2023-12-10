from sqlalchemy.orm import Session

from models.core import Producer


def get_producers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Producer).order_by(Producer.id).offset(skip).limit(limit).all()
