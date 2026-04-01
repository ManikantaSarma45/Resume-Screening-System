import os
from fastapi import APIRouter, UploadFile, File, Depends
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.models.resume import Resume
from app.schemas.resume import ResumeOut
from app.services.resume_parser import extract_text_from_pdf

router = APIRouter()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/upload", response_model=ResumeOut)
def upload_resume(
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    # Save file
    with open(file_path, "wb") as f:
        f.write(file.file.read())

    # Extract text
    extracted_text = extract_text_from_pdf(file_path)

    # Save to DB
    db_resume = Resume(
        filename=file.filename,
        content=extracted_text
    )
    db.add(db_resume)
    db.commit()
    db.refresh(db_resume)

    return db_resume


@router.get("/", response_model=list[ResumeOut])
def get_resumes(db: Session = Depends(get_db)):
    return db.query(Resume).all()
