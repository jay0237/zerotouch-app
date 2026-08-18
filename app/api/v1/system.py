from fastapi import APIRouter
from datetime import datetime, timezone
import os

router = APIRouter(prefix="/api/v1", tags=["System"])


@router.get("/health")
def health():
    return {
        "status": "healthy",
        "service": "zerotouch",
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }


@router.get("/ready")
def readiness():
    return {
        "status": "ready",
        "service": "zerotouch",
    }


@router.get("/info")
def info():
    return {
        "service": os.getenv("APP_NAME", "ZeroTouch"),
        "version": os.getenv("APP_VERSION", "1.0.0"),
        "environment": os.getenv("APP_ENV", "development"),
    }