from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from models import schemes

from views.laptops import get_laptops
from controllers.laptops import add_laptop
from models.database import get_db


router = APIRouter()

@router.get('/', response_model=list[schemes.Laptop])
def get_laptops_routed(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    laptops = get_laptops(db, skip=skip, limit=limit)
    return laptops

@router.post('/', response_model=schemes.Laptop, status_code=201)
def add_laptop_routed(laptop_data: schemes.LaptopCreate, db: Session = Depends(get_db)):
    return add_laptop(db, laptop_data=laptop_data)
