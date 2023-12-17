from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session
from starlette.status import HTTP_400_BAD_REQUEST

from models.core import Laptop
from models.schemes import LaptopCreate

from .tools import commit_before_return


@commit_before_return
def add_laptop(db: Session, laptop_data: LaptopCreate):
    if db.scalar(select(Laptop).where(Laptop.model == laptop_data.model)):
        raise HTTPException(
            status_code=HTTP_400_BAD_REQUEST, detail="The laptop already exists"
        )
    laptop = Laptop(
        cpu=laptop_data.cpu,
        model=laptop_data.model,
        gpu=laptop_data.gpu,
        screen_size=laptop_data.screen_size,
        memory=laptop_data.memory,
    )
    db.add(laptop)
    return laptop


@commit_before_return
def delete_laptop(db: Session, id: int):
    laptop = db.query(Laptop).filter(Laptop.id == id).delete()
    return laptop
