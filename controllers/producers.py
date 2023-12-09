from typing import Optional
from sqlalchemy.orm import Session

from models.core import Producer
from models.schemes import ProducerCreate

from .tools import commit_before_return


@commit_before_return
def add_producer(db: Session, producer_data: ProducerCreate):
    producer = Producer(
        name=producer_data.name,
        guarantee=producer_data.guarantee,
        country=producer_data.country,
        place=producer_data.place,
    )
    db.add(producer)
    return producer


def get_producer(db: Session, id: int):
    return db.query(Producer).filter(Producer.id == id)


@commit_before_return
def update_producer(
        db: Session, id, producer_data: ProducerCreate
):
    producer = get_producer(db, id).first()
    producer.guarantee = producer_data.guarantee
    producer.country = producer_data.country
    producer.place = producer_data.place

    db.add(producer)
    return db


@commit_before_return
def delete_producer(db: Session, id: int):
    producer = get_producer(db, id).delete()
    return producer
