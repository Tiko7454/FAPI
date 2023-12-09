from sqlalchemy.orm import Session

from models.core import MarketOffer
from models.schemes import MarketOfferCreate

from .tools import commit_before_return


@commit_before_return
def add_market_offer(db: Session, market_offer_data: MarketOfferCreate):
    market_offer = MarketOffer(
        volume=market_offer_data.volume,
        date=market_offer_data.date,
        cost=market_offer_data.cost,
        laptop_id=market_offer_data.laptop_id,
        producer_id=market_offer_data.producer_id,
    )
    db.add(market_offer)
    return market_offer
