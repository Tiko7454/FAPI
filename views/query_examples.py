from sqlalchemy.orm import Session
from sqlalchemy.sql import func

from models.core import Producer, Laptop


def select_where(db: Session, skip: int, limit: int, order_by: str):
    query = (
        db.query(Producer)
        .where(Producer.country == "United States")
        .where(Producer.guarantee > 1)
    )
    match order_by:
        case "id":
            query = query.order_by(Producer.id)
        case "name":
            query = query.order_by(Producer.name)
        case "guarantee":
            query = query.order_by(Producer.guarantee)
        case "place":
            query = query.order_by(Producer.place)
        case _:
            raise ValueError("Unexpected order_by")
    return query.offset(skip).limit(limit).all()


def join(db: Session, skip: int, limit: int, order_by: str):
    ...


def group_by(db: Session, skip: int, limit: int):
    """groups laptop screen_size and computes their avarage memory"""
    query = (
        db.query(
            Laptop.screen_size, func.sum(Laptop.memory) / func.count(Laptop.memory)
        )
        .group_by(Laptop.screen_size)
        .order_by(Laptop.screen_size)
    )
    return query.offset(skip).limit(limit).all()
