from sqlalchemy.orm import Session

from models import core


def get_producers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(core.Producer).offset(skip).limit(limit).all()
