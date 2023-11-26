from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from model import schemes

from views.producers import get_producers
from model.database import get_db


router = APIRouter()

@router.get('/', response_model=list[schemes.Producer])
def read_producers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    producers = get_producers(db, skip=skip, limit=limit)
    return producers
