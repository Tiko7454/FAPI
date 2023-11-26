from fastapi import FastAPI
from model import core
from model.database import engine
from routers.laptops import router as laptops_router
from routers.producers import router as producers_router
from routers.market_offers import router as market_offers_router

core.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router=laptops_router, prefix="/laptops")
app.include_router(router=producers_router, prefix="/producers")
app.include_router(router=market_offers_router, prefix="/market_offers")
