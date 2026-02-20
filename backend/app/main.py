from fastapi import FastAPI
from backend.app.api.v1.router import api_router
from backend.app.db.init_db import init_db

app = FastAPI(title="Resume Screening System")

@app.on_event("startup")
def startup():
    init_db()

app.include_router(api_router, prefix="/api/v1")

@app.get("/health")
def health():
    return {"status": "ok"}
