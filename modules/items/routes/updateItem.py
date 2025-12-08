# modules/items/routes/updateItem.py

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from database import get_db
from modules.items.schema.models import MentalHealthResponse
from modules.items.schema.schemas import MentalHealthUpdate, MentalHealthOut
from modules.items.scripts.cleaning import normalisasi  #tambah ini

router = APIRouter(
    prefix="/mental-health",
    tags=["mental_health_update"],
)

@router.put("/responses/{response_id}", response_model=MentalHealthOut)
def update_response(
    response_id: int,
    payload: MentalHealthUpdate,
    db: Session = Depends(get_db),
):
    """
    Memperbarui statement dan/atau status untuk id tertentu.
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

    #kalau statement diubah -> bersihkan lagi
    if payload.statement is not None:
        obj.statement = payload.statement
        obj.clean_statement = normalisasi(payload.statement)

    if payload.status is not None:
        obj.status = payload.status

    db.commit()
    db.refresh(obj)
    return obj