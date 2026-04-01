from sqlalchemy import Column, Integer, String, Text
from app.db.base import Base


class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(Text, nullable=True)

    # NEW FIELDS
    must_have = Column(Text, nullable=True)       # comma separated
    good_to_have = Column(Text, nullable=True)    # comma separated
