from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from views.ui import homepage

router = APIRouter()


@router.get("/", response_class=HTMLResponse)
def homepage_routed():
    return homepage()
