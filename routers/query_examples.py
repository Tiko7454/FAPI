from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from models import schemes

from views.query_examples import select_where, join, group_by
from controllers.query_examples import update

from models.database import get_db


router = APIRouter()


@router.get("/select_where", response_model=list[schemes.Producer])
def select_where_routed(
    skip: int = 0, limit: int = 100, order_by: str = "id", db: Session = Depends(get_db)
):
    return select_where(db, skip=skip, limit=limit, order_by=order_by)


@router.get("/join", response_model=list[tuple[schemes.Laptop, schemes.Producer]])
def join_routed(
    skip: int = 0,
    limit: int = 100,
    order_by: str = "laptop_id",
    db: Session = Depends(get_db),
):
    return join(db, skip=skip, limit=limit, order_by=order_by)


@router.put("/update")
def update_routed(db: Session = Depends(get_db)):
    return update(db)


@router.get("/group_by", response_model=list[dict[str, float]])
def group_by_routed(skip: int = 0, limit: int = 200, db: Session = Depends(get_db)):
    return group_by(db, skip=skip, limit=limit)
