from fastapi import FastAPI

from app.api.v1.endpoints import prayers
from app.core.database import Base, engine

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Catholic API",
    description="API for Catholic prayers and resources",
    version="0.1.0",
)

app.include_router(prayers.router, prefix="/api/v1/prayers", tags=["prayers"])
