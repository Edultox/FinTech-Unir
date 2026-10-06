from contextlib import asynccontextmanager

from fastapi import FastAPI
from app.routers.users_router import router as users_router
from app.db.database import init_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield


def create_app() -> FastAPI:
    app = FastAPI(lifespan=lifespan)
    app.include_router(users_router)
    return app
