from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from model import schemes

from controllers.market_offers import get_market_offers
from model.database import get_db


router = APIRouter()

@router.get('/', response_model=list[schemes.MarketOffer])
def read_market_offers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    market_offers = get_market_offers(db, skip=skip, limit=limit)
    return market_offers
