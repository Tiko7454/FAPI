from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from models import schemes

from views.producers import get_producers
from controllers.producers import (
    add_producer,
    update_producer,
    delete_producer,
)
from models.database import get_db


router = APIRouter()


@router.get("/", response_model=list[schemes.Producer])
def read_producers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    producers = get_producers(db, skip=skip, limit=limit)
    return producers


@router.post("/", response_model=schemes.Producer, status_code=201)
def add_producer_routed(
    producer_data: schemes.ProducerCreate, db: Session = Depends(get_db)
):
    return add_producer(db, producer_data=producer_data)


@router.put("/{id}")
def update(
    id: int, producer_data: schemes.ProducerCreate, db: Session = Depends(get_db)
):
    return update_producer(db, id=id, producer_data=producer_data)


@router.delete("/{id}")
def delete(id: int, db: Session = Depends(get_db)):
    return delete_producer(db, id=id)
