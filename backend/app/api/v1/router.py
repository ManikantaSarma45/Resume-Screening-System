from fastapi import APIRouter
from app.api.v1.endpoints import auth, jobs, resumes, ranking

api_router = APIRouter()

api_router.include_router(auth.router, prefix="/auth", tags=["Auth"])
api_router.include_router(jobs.router, prefix="/jobs", tags=["Jobs"])
api_router.include_router(resumes.router, prefix="/resumes", tags=["Resumes"])
api_router.include_router(ranking.router, prefix="/ranking", tags=["Ranking"])
