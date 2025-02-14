from fastapi import FastAPI
from app.api.v1.endpoints.premium import router as premium_router

app = FastAPI(title="Car Insurance Premium")

app.include_router(premium_router, prefix="/api/v1", tags=["premium"])
