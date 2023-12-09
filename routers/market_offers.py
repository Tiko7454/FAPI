from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from models import schemes

from views.market_offers import get_market_offers
from controllers.market_offers import (
    add_market_offer,
    update_market_offer,
    delete_market_offer,
)
from models.database import get_db


router = APIRouter()


@router.get("/", response_model=list[schemes.MarketOffer])
def read_market_offers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    market_offers = get_market_offers(db, skip=skip, limit=limit)
    return market_offers


@router.post("/", response_model=schemes.MarketOffer, status_code=201)
def add_market_offer_routed(
    market_offer_data: schemes.MarketOfferCreate, db: Session = Depends(get_db)
):
    return add_market_offer(db, market_offer_data=market_offer_data)


@router.put("/{id}")
def update(
    id: int, market_offer_data: schemes.MarketOfferCreate, db: Session = Depends(get_db)
):
    return update_market_offer(db, id=id, market_offer_data=market_offer_data)


@router.delete("/{id}")
def delete(id: int, db: Session = Depends(get_db)):
    return delete_market_offer(db, id=id)
