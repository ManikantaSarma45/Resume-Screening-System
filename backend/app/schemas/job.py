from pydantic import BaseModel
from typing import Optional


class JobCreate(BaseModel):
    title: str
    description: Optional[str] = None
    must_have: Optional[str] = None
    good_to_have: Optional[str] = None


class JobOut(JobCreate):
    id: int

    class Config:
        from_attributes = True
