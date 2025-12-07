from fastapi import APIRouter, HTTPException
from .schemas import PredictRequest, PredictResponse
from .services.predict_xgb import predict_text
from .validator import validate_english_text_strict

router = APIRouter(prefix="/ml", tags=["Machine Learning"])

@router.post("/predict", response_model=PredictResponse)
def predict(req: PredictRequest):

    valid, msg = validate_english_text_strict(req.text)
    if not valid:
        raise HTTPException(status_code=400, detail=msg)

    result = predict_text(req.text)
    return PredictResponse(label=result)
