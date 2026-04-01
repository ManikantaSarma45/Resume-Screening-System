from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from backend.app.api.v1.router import api_router
from backend.app.db.init_db import init_db

app = FastAPI(title="Resume Screening System")

# =========================
# ✅ STARTUP
# =========================
@app.on_event("startup")
def startup():
    init_db()

# =========================
# ✅ CORS
# =========================
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# =========================
# ✅ API ROUTES (IMPORTANT)
# =========================
app.include_router(api_router, prefix="/api/v1")

# =========================
# ✅ STATIC FILES
# =========================
app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")

# =========================
# ✅ HEALTH CHECK
# =========================
@app.get("/health")
def health():
    return {"status": "ok"}