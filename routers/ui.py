from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from views.ui import homepage, tablepage

router = APIRouter()


@router.get("/", response_class=HTMLResponse)
def homepage_routed():
    return homepage()


@router.get("/laptops", response_class=HTMLResponse)
def laptops_routed():
    return tablepage("laptops")


@router.get("/producers", response_class=HTMLResponse)
def producers_routed():
    return tablepage("producers")


@router.get("/market_offers", response_class=HTMLResponse)
def market_offers_routed():
    return tablepage("market_offers")
