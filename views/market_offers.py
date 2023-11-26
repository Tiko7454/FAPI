from sqlalchemy.orm import Session

from models import core


def get_market_offers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(core.MarketOffer).offset(skip).limit(limit).all()
