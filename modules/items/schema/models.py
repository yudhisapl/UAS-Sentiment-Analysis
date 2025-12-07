from sqlalchemy import Column, Integer, String, Text
from database import Base

# Model ORM untuk tabel mental_health_responses
class MentalHealthResponse(Base):
    __tablename__ = "mental_health_responses"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    statement = Column(Text, nullable=False)
    status = Column(String(50), nullable=False, index=True)
