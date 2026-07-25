from fastapi import APIRouter

router = APIRouter()

@router.get("/health")
def health():
    return {
        "status": "healthy"
    }

@router.get("/live")
def live():
    return {
        "status": "alive",
    }

@router.get("/ready")
def ready():
    return {
        "status": "ready",
    }