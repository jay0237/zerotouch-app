from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def root():
    return {
        "project": "ZeroTouch",
        "message": "Welcome to ZeroTouch API",
        "status": "running"
    }