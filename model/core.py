from sqlalchemy import Column, ForeignKey, Integer, String, Double, Date
from sqlalchemy.orm import relationship

from .database import Base


class Laptop(Base):
    __tablename__ = "laptops"

    id = Column(Integer, primary_key=True, index=True)
    cpu = Column(String)
    gpu = Column(String)
    model = Column(String, unique=True, index=True)
    screen_size = Column(Double)
    memory = Column(Integer)

    market_offers = relationship("MarketOffer", back_populates="laptop")


class Producer(Base):
    __tablename__ = "producer"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    guarantee = Column(Integer)
    country = Column(String)
    place = Column(String)

    market_offers = relationship("MarketOffer", back_populates="producer")


class MarketOffer(Base):
    __tablename__ = "market_offers"

    id = Column(Integer, primary_key=True, index=True)
    volume = Column(Integer)
    date = Column(Date)
    cost = Column(Double)

    laptop = relationship("Laptop", back_populates="market_offers")
    producer = relationship("Producer", back_populates="market_offers")
