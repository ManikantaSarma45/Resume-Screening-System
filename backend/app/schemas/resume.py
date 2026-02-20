from pydantic import BaseModel

class ResumeOut(BaseModel):
    id: int
    filename: str
    content: str

    class Config:
        from_attributes = True
