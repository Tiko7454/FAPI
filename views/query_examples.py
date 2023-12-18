from sqlalchemy.orm import Session
from sqlalchemy.sql import func

from models.core import MarketOffer, Producer, Laptop


def select_where(db: Session, skip: int, limit: int, order_by: str):
    """gets every producer from the USA with a guarantee greater than 2"""
    query = (
        db.query(Producer)
        .where(Producer.country == "United States")
        .where(Producer.guarantee > 2)
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
    """returns pair of laptop and producer which were connected by a market offer"""
    query = (
        db.query(MarketOffer, Laptop, Producer)
        .join(Laptop, Laptop.id == MarketOffer.laptop_id)
        .join(Producer, Producer.id == MarketOffer.producer_id)
    )
    match order_by:
        case "laptop_id":
            query = query.order_by(Laptop.id)
        case "producer_id":
            query = query.order_by(Producer.id)
        case _:
            raise ValueError("Unexpected order_by")
    query = query.offset(skip).limit(limit).all()
    return [(laptop, producer) for _, laptop, producer in query]


def group_by(db: Session, skip: int, limit: int):
    """groups laptop screen_size and computes their avarage memory"""
    query = (
        db.query(Laptop.screen_size, func.avg(Laptop.memory))
        .group_by(Laptop.screen_size)
        .order_by(Laptop.screen_size)
    )
    res = []
    for screen_size, avg in query.offset(skip).limit(limit).all():
        res.append({"screen_size": screen_size, "avg": avg})
    return res
