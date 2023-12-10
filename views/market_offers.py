from sqlalchemy.orm import Session

from models.core import MarketOffer


def get_market_offers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(MarketOffer).order_by(MarketOffer.id).offset(skip).limit(limit).all()
