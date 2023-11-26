from sqlalchemy import Column, ForeignKey, Integer, String, Date, Numeric
from sqlalchemy.orm import mapped_column, relationship

from .database import Base


class MarketOffer(Base):
    __tablename__ = "market_offers"

    id = Column(Integer, primary_key=True, index=True)
    volume = Column(Integer)
    date = Column(Date)
    cost = Column(Numeric)

    # Many-to-one
    laptop_id = mapped_column(ForeignKey("laptops.id"))
    laptop = relationship("Laptop", back_populates="market_offers")

    # Many-to-one
    producer_id = mapped_column(ForeignKey("producers.id"))
    producer = relationship("Producer", back_populates="market_offers")


class Laptop(Base):
    __tablename__ = "laptops"

    id = Column(Integer, primary_key=True, index=True)
    cpu = Column(String)
    gpu = Column(String)
    model = Column(String, unique=True, index=True)
    screen_size = Column(Numeric)
    memory = Column(Integer)

    # One-to-many
    market_offers = relationship(MarketOffer, back_populates="laptop")


class Producer(Base):
    __tablename__ = "producers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    guarantee = Column(Integer)
    country = Column(String)
    place = Column(String)

    # One-to-many
    market_offers = relationship(MarketOffer, back_populates="producer")
