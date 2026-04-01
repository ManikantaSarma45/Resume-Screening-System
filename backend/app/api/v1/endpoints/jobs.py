from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import Optional

from app.api.deps import get_db
from app.models.job import Job
from app.schemas.job import JobCreate, JobOut

router = APIRouter()


# -------------------------------
# Utility: Normalize skill string
# -------------------------------
def clean_string(value: Optional[str]) -> Optional[str]:
    if not value:
        return None

    # lower case + remove extra spaces
    cleaned = [s.strip().lower() for s in value.split(",") if s.strip()]
    return ",".join(cleaned)


# -------------------------------
# Create Job
# -------------------------------
@router.post("/", response_model=JobOut)
def create_job(job: JobCreate, db: Session = Depends(get_db)):

    db_job = Job(
        title=job.title,
        description=job.description,
        must_have=clean_string(job.must_have),
        good_to_have=clean_string(job.good_to_have)
    )

    db.add(db_job)
    db.commit()
    db.refresh(db_job)

    return db_job


# -------------------------------
# Get All Jobs
# -------------------------------
@router.get("/", response_model=list[JobOut])
def get_jobs(db: Session = Depends(get_db)):
    return db.query(Job).all()


# -------------------------------
# Get Single Job
# -------------------------------
@router.get("/{job_id}", response_model=JobOut)
def get_job(job_id: int, db: Session = Depends(get_db)):

    job = db.query(Job).filter(Job.id == job_id).first()

    if not job:
        return {"error": "Job not found"}

    return job
