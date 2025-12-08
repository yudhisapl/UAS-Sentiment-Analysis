# modules/items/routes/createItem.py

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from database import get_db
from modules.items.schema.models import MentalHealthResponse
from modules.items.schema.schemas import MentalHealthCreate, MentalHealthOut
from modules.items.scripts.cleaning import normalisasi  #tambah ini

router = APIRouter(
    prefix="/mental-health",
    tags=["mental_health_create"],
)

@router.post(
    "/responses",
    response_model=MentalHealthOut,
    status_code=status.HTTP_201_CREATED,
)
def create_response(payload: MentalHealthCreate, db: Session = Depends(get_db)):
    """
    Menambahkan satu data baru ke tabel mental_health_responses.
    """
    #langsung normalisasi teks input
    clean_text = normalisasi(payload.statement)

    obj = MentalHealthResponse(
        statement=payload.statement,
        clean_statement=clean_text,   #simpan teks bersih juga
        status=payload.status,
    )
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj