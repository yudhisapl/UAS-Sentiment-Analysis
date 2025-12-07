# modules/items/routes/readItem.py

from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from database import get_db
from modules.items.schema.models import MentalHealthResponse
from modules.items.schema.schemas import MentalHealthOut

router = APIRouter(
    prefix="/mental-health",
    tags=["mental_health_read"],
)


@router.get("/responses", response_model=List[MentalHealthOut])
def read_all_responses(db: Session = Depends(get_db)):
    """
    Mengembalikan seluruh baris tabel mental_health_responses.
    (Untuk dataset besar, sebaiknya tambahkan pagination.)
    """
    data = db.query(MentalHealthResponse).all()
    return data


@router.get("/responses/{response_id}", response_model=MentalHealthOut)
def read_response_by_id(response_id: int, db: Session = Depends(get_db)):
    """
    Mengembalikan satu baris berdasarkan id.
    """
    obj = (
        db.query(MentalHealthResponse)
        .filter(MentalHealthResponse.id == response_id)
        .first()
    )
    if not obj:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Response dengan id={response_id} tidak ditemukan.",
        )
    return obj
