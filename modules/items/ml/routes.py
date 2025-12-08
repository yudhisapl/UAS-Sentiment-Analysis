from fastapi import APIRouter, HTTPException
from .schemas import PredictRequest, PredictResponse
from .services.predict_xgb import predict_text

router = APIRouter(prefix="/ml", tags=["Machine Learning"])

@router.post("/predict", response_model=PredictResponse)
def predict(req: PredictRequest):
    result = predict_text(req.text)
    return PredictResponse(label=result)

