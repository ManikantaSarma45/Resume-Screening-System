# Resume Screening System

This project is a web application for managing job descriptions, uploading resumes, and ranking candidates based on job requirements.

---

## Tech Stack

Frontend: HTML, CSS, JavaScript  
Backend: FastAPI (Python)  
Database: PostgreSQL  
Containerization: Docker and Docker Compose  

---

## Project Structure

resume-screening-system/

backend/ → FastAPI backend  
frontend/ → Static frontend files  
docker-compose.yml  
.env  
README.md  

---

## How to Run the Project

1. Clone the repository

git clone https://github.com/ManikantaSarma45/Resume-Screening-System.git  
cd Resume-Screening-System  

2. Run using Docker

docker-compose up --build  

---

## Application URLs

Frontend: http://localhost:3000/upload.html  
Backend: http://localhost:8000/docs  

---

## Features

Upload resumes in PDF format  
Create and manage job descriptions  
Store resume data  
Rank resumes based on job criteria  

---

## Database

PostgreSQL is used as the database.

Tables:
Users  
Jobs  
Resumes  
Scores  

---

## Environment Variables

Example .env file:

DATABASE_URL=postgresql://postgres:postgres@db:5432/ats_db  

---

## Notes

Backend runs on port 8000  
Frontend runs on port 3000  
API base URL: http://localhost:8000/api/v1  

---

## Author

Manikanta Sarma and harsha
https://github.com/ManikantaSarma45