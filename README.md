# ATS Resume Screening System

## Features
- Resume Upload
- Job Creation
- Resume Ranking (Matching Score)

## Tech Stack
- FastAPI
- PostgreSQL
- HTML, Tailwind, JS
## How to Run
**1.Clone the Repository**
git clone https://github.com/ManikantaSarma45/Resume-Screening-System.git
cd Resume-Screening-System
**2. Setup Backend (FastAPI)**
cd backend
python3 -m venv venv
source venv/bin/activate   # Mac/Linux
pip install -r requirements.txt
**3.Setup Database (PostgreSQL)**
DATABASE_URL=postgresql://username:password@localhost/dbname
**4.Run Backend Server**
uvicorn app.main:app --reload
http://127.0.0.1:8000
http://127.0.0.1:8000/docs
**5.Open Frontend**
Then open in browser:
upload.html
jobs.html
ranking.html
**6.Features to Test**
Upload Resume (PDF)
View Resumes
Create Jobs
Rank Candidate
**Notes**
Backend runs on: http://127.0.0.1:8000
API prefix: /api/v1
Uploads stored in /uploads
