# main.py

from fastapi import FastAPI

from database import Base, engine
from modules.items.schema.models import MentalHealthResponse  # registrasi metadata tabel
from modules.items.routes import (
    readItem,
    createItem,
    updateItem,
    deleteItem,
    analytics
)

# === Tambahkan import ML router di sini ===
from modules.items.ml.routes import router as ml_router


# --- Inisialisasi database ---
Base.metadata.create_all(bind=engine)

# --- FastAPI app ---
app = FastAPI(
    title="Mental Health Sentiment API",
    description="API untuk mengakses tabel mental_health_responses (statement + status).",
    version="1.0.0",
)

# --- Registrasi router CRUD ---
app.include_router(readItem.router)
app.include_router(createItem.router)
app.include_router(updateItem.router)
app.include_router(deleteItem.router)
app.include_router(analytics.router)

# --- Registrasi router ML (PREDIKSI TEKS) ---
app.include_router(ml_router)

# --- Root endpoint ---
@app.get("/", include_in_schema=False)
def root():
    return {"message": "Mental Health Sentiment API is running"}
