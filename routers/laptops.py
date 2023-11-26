from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from model import schemes

from views.laptops import get_laptops
from model.database import get_db


router = APIRouter()

@router.get('/', response_model=list[schemes.Laptop])
def read_laptops(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    laptops = get_laptops(db, skip=skip, limit=limit)
    return laptops
