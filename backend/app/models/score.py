from sqlalchemy import Column, Integer, Float
from backend.app.db.base import Base

class Score(Base):
    __tablename__ = "scores"

    id = Column(Integer, primary_key=True, index=True)
    job_id = Column(Integer, nullable=False)
    resume_id = Column(Integer, nullable=False)
    score = Column(Float, nullable=False)
