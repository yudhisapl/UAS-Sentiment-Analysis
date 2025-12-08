# modules/items/routes/createItem.py

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from database import get_db
from modules.items.schema.models import MentalHealthResponse
from modules.items.schema.schemas import MentalHealthCreate, MentalHealthOut
from modules.items.ml.services.predict_xgb import predict_text

router = APIRouter(
    prefix="/mental-health",
    tags=["mental_health_create"],
)


def _to_out(obj: MentalHealthResponse) -> MentalHealthOut:
    """
    Helper untuk mengubah ORM object menjadi output sesuai flowchart.
    """
    status_initial = predict_text(obj.statement)
    status_final = obj.status

    return MentalHealthOut(
        id=obj.id,
        statement=obj.statement,
        status_initial=status_initial,
        status_final=status_final,
    )


@router.post(
    "/responses",
    response_model=MentalHealthOut,
    status_code=status.HTTP_201_CREATED,
)
def create_response(
    payload: MentalHealthCreate,
    db: Session = Depends(get_db),
):
    """
    Menambahkan satu data baru ke tabel mental_health_responses.

    Flow:
    1. Admin memasukkan statement pasien.
    2. Sistem memanggil model ML untuk mendapatkan diagnosa awal (status_initial).
    3. Nilai diagnosa awal disimpan di kolom 'status' (sebagai diagnosa awal / sementara).
    """
    # Prediksi diagnosa awal dengan model ML
    status_initial = predict_text(payload.statement)

    obj = MentalHealthResponse(
        statement=payload.statement,
        status=status_initial,  # simpan diagnosa awal ke kolom status
    )

    db.add(obj)
    db.commit()
    db.refresh(obj)

    return _to_out(obj)