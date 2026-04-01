from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.models.job import Job
from app.models.resume import Resume
from app.models.score import Score
from app.services.ranking import hybrid_rank

router = APIRouter()


@router.post("/rank/{job_id}")
def rank_for_job(job_id: int, db: Session = Depends(get_db)):

    job = db.query(Job).filter(Job.id == job_id).first()
    if not job:
        return {"error": "Job not found"}

    resumes = db.query(Resume).all()
    if not resumes:
        return {"error": "No resumes available"}

    # Remove old scores
    db.query(Score).filter(Score.job_id == job_id).delete()
    db.commit()

    results = []

    for resume in resumes:
        scores = hybrid_rank(job, resume.content)


        db_score = Score(
            job_id=job.id,
            resume_id=resume.id,
            score=float(scores["final_score"])  # ensure pure Python float
        )

        db.add(db_score)

        results.append({
            "resume_id": resume.id,
            "filename": resume.filename,
            **scores
        })

    db.commit()

    results.sort(key=lambda x: x["final_score"], reverse=True)

    return results
