from fastapi import FastAPI
from contextlib import asynccontextmanager
from src.db.connect import init_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("server is starting")
    await init_db()
    yield
    print("server is shutting down")


app = FastAPI(
    title="Book service",
    version="0.1.0",
    description="A simple web service for a book application",
    lifespan=lifespan,
)


@app.get("/")
async def read_root():
    return {"Hello": "World"}


# app.include_router(route, tags=["books"])
