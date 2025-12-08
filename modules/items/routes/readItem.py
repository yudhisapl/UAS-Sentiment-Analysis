# modules/items/routes/readItem.py

from typing import List

from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session

from database import get_db
from modules.items.schema.models import MentalHealthResponse
from modules.items.schema.schemas import MentalHealthOut
from modules.items.ml.services.predict_xgb import predict_text

router = APIRouter(
    prefix="/mental-health",
    tags=["mental_health_read"],
)


def _to_out(obj: MentalHealthResponse) -> MentalHealthOut:
    """
    Konversi 1 baris data ke bentuk output yang berisi:
    id, statement, status_initial (ML), status_final (DB).
    """
    status_initial = predict_text(obj.statement)
    status_final = obj.status

    return MentalHealthOut(
        id=obj.id,
        statement=obj.statement,
        status_initial=status_initial,
        status_final=status_final,
    )


@router.get("/responses", response_model=List[MentalHealthOut])
def read_all_responses(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=100),
    db: Session = Depends(get_db),
):
    data = (
        db.query(MentalHealthResponse)
        .order_by(MentalHealthResponse.id)
        .offset(skip)
        .limit(limit)
        .all()
    )
    return [_to_out(obj) for obj in data]


@router.get("/responses/{response_id}", response_model=MentalHealthOut)
def read_response_by_id(
    response_id: int,
    db: Session = Depends(get_db),
):
    """
    Mengembalikan satu baris berdasarkan id.
    Digunakan pada step 'Psikolog verifikasi id statement (data pasien)'.
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

    return _to_out(obj)
