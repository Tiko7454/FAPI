from fastapi import FastAPI
from models import core
from models.database import engine
from routers.ui import router as ui_router
from routers.laptops import router as laptops_router
from routers.producers import router as producers_router
from routers.market_offers import router as market_offers_router
from routers.query_examples import router as query_examples_router

core.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router=ui_router, prefix="/homepage")
app.include_router(router=laptops_router, prefix="/laptops")
app.include_router(router=producers_router, prefix="/producers")
app.include_router(router=market_offers_router, prefix="/market_offers")
app.include_router(router=query_examples_router, prefix="/query_examples")
