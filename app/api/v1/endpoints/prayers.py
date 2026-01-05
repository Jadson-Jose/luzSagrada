from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

# Importe diretamente do arquivo prayer.py, não do pacote schemas
from app.schemas.prayer import PrayerCreate, PrayerResponse
from app.models.prayer import Prayer
from app.core.database import get_db

router = APIRouter()

@router.get("/", response_model=List[PrayerResponse])
def read_prayers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    prayers = db.query(Prayer).offset(skip).limit(limit).all()
    return prayers

@router.post("/", response_model=PrayerResponse, status_code=201)
def create_prayer(prayer: PrayerCreate, db: Session = Depends(get_db)):
    db_prayer = Prayer(**prayer.model_dump())
    db.add(db_prayer)
    db.commit()
    db.refresh(db_prayer)
    return db_prayer
