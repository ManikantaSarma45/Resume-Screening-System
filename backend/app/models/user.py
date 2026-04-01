from sqlalchemy import Column, Integer, String
from app.db.base import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    # Email
    email = Column(String(255), unique=True, index=True, nullable=False)

    # IMPORTANT: Must be large enough for bcrypt hash (~60 chars)
    hashed_password = Column(String(255), nullable=False)