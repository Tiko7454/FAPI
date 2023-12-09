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
