from sqlalchemy.orm import Session

from database import SessionLocal
from modules.items.schema.models import MentalHealthResponse
from modules.items.scripts.cleaning import normalisasi   

def main():
    db: Session = SessionLocal()
    try:
        rows = db.query(MentalHealthResponse).all()
        for row in rows:
            row.clean_statement = normalisasi(row.statement)
        db.commit()
    finally:
        db.close()

if __name__ == "__main__":
    main()
