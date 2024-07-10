from app.api.routes.router import base_router as router
from app.database.session import sessionmanager
from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.database.tables import create_tables

@asynccontextmanager
async def lifespan(_app: FastAPI):
    """
    handles startup and shutdown events
    """
    yield
    if sessionmanager.engine is not None:
        await sessionmanager.close()


app = FastAPI()
app.include_router(router)

@app.on_event("startup")
async def startup_event():
    await create_tables()
