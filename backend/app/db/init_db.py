from backend.app.db.session import engine
from backend.app.db.base import Base

from backend.app.models.user import User
from backend.app.models.job import Job
from backend.app.models.resume import Resume
from backend.app.models.score import Score

def init_db():
    Base.metadata.create_all(bind=engine)
