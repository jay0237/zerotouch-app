from fastapi import APIRouter
from app.schemas.health import (
    HealthResponse,
    LiveResponse,
    ReadyResponse,
)
router = APIRouter()

@router.get("/health", response_model=HealthResponse)
def health():
    return HealthResponse(
        status="healthy",
        service=settings.APP_NAME,
    )

@router.get("/live", response_model=LiveResponse)
def live():
    return LiveResponse(
        status="alive",
    )

@router.get("/ready", response_model=ReadyResponse)
def ready():
    return ReadyResponse(
        status="ready",
    )