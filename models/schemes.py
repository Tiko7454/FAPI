from datetime import date
from pydantic import BaseModel


class MarketOfferBase(BaseModel):
    volume: int
    date: date
    cost: float
    laptop_id: int
    producer_id: int


class MarketOfferCreate(MarketOfferBase):
    pass


class MarketOffer(MarketOfferBase):
    id: int

    class Config:
        from_attributes = True


class LaptopBase(BaseModel):
    model: str
    cpu: str
    gpu: str
    screen_size: float
    memory: int


class LaptopCreate(LaptopBase):
    pass


class Laptop(LaptopBase):
    id: int
    market_offers: list[MarketOffer]

    class Config:
        from_attributes = True


class ProducerBase(BaseModel):
    name: str
    guarantee: int
    country: str
    place: str


class ProducerCreate(ProducerBase):
    pass


class Producer(ProducerBase):
    id: int
    market_offers: list[MarketOffer]

    class Config:
        from_attributes = True
