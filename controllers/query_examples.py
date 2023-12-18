from sqlalchemy.orm import Session

from models.core import Producer

from .tools import commit_before_return


@commit_before_return
def update(db: Session):
    """Decrements producer guarantees if they exceed 2"""
    db.query(Producer).filter(Producer.guarantee > 2).update(
        {"guarantee": Producer.guarantee - 1}
    )
    return db
