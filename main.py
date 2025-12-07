# main.py

from fastapi import FastAPI

from database import Base, engine
from modules.items.schema.models import MentalHealthResponse  # registrasi metadata tabel
from modules.items.routes import (
    readItem,
    createItem,
    updateItem,
    deleteItem,
)

# --- Inisialisasi database (buat tabel kalau belum ada) ---
Base.metadata.create_all(bind=engine)

# --- Inisialisasi FastAPI app (WAJIB bernama "app") ---
app = FastAPI(
    title="Mental Health Sentiment API",
    description="API untuk mengakses tabel mental_health_responses (statement + status).",
    version="1.0.0",
)


# --- Registrasi router ---
app.include_router(readItem.router)
app.include_router(createItem.router)
app.include_router(updateItem.router)
app.include_router(deleteItem.router)


# --- Root endpoint sederhana ---
@app.get("/")
def root():
    return {"message": "Mental Health Sentiment API is running"}
