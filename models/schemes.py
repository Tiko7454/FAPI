from pydantic import BaseModel


class MarketOfferBase(BaseModel):
    volume: int
    date: str
    cost: float
    pass


class MarketOfferCreate(MarketOfferBase):
    pass


class MarketOffer(MarketOfferBase):
    id: int
    laptop_id: int  # TODO: check if it works
    producer_id: int  # TODO: check if it works

    class Config:
        from_attributes = True


class LaptopBase(BaseModel):
    cpu: str
    gpu: str
    model: str
    screen_size: float
    memory: int


class LaptopCreate(LaptopBase):
    pass


class Laptop(BaseModel):
    id: int
    market_offers: list[MarketOffer]  # TODO: check if it works

    class Config:
        from_attributes = True


class ProducerBase(BaseModel):
    name: str
    guarantee: int
    country: str
    place: str


class ProducerCreate(ProducerBase):
    pass


class Producer(BaseModel):
    id: int
    market_offers: list[MarketOffer]  # TODO: check if it works

    class Config:
        from_attributes = True
