# modules/items/routes/deleteItem.py

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from database import get_db
from modules.items.schema.models import MentalHealthResponse

router = APIRouter(
    prefix="/mental-health",
    tags=["mental_health_delete"],
)


@router.delete(
    "/responses/{response_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_response(response_id: int, db: Session = Depends(get_db)):
    """
    Menghapus baris berdasarkan id.
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

    db.delete(obj)
    db.commit()
    # Tidak perlu return body untuk 204
