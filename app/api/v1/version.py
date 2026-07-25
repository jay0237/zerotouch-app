from fastapi import APIRouter

router = APIRouter()

@router.get("/version")
def version():
    return {
        "version": "0.1.0"
    }