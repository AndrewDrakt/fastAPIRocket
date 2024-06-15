from fastapi import FastAPI
from contextlib import asynccontextmanager
from router import router as post_router
from database import *

@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print("Database cleared")
    await create_tables()
    print("Database ready to work")
    yield
    print("Database shutting down")

app = FastAPI(lifespan=lifespan)
app.include_router(post_router)
