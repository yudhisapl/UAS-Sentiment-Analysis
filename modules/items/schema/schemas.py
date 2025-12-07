from pydantic import BaseModel
from typing import Optional


class MentalHealthBase(BaseModel):
    statement: str
    status: str


class MentalHealthCreate(MentalHealthBase):
    """Dipakai di endpoint POST (insert data baru)."""
    pass


class MentalHealthUpdate(BaseModel):
    """Dipakai di endpoint PUT/PATCH (update data)."""
    statement: Optional[str] = None
    status: Optional[str] = None


class MentalHealthOut(MentalHealthBase):
    id: int

    class Config:
        orm_mode = True