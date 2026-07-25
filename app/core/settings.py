from fastapi import APIRouter

from app.core.settings import settings

router = APIRouter()

@router.get("/version")
def version():
    return{
        "application": setttings.APP_NAME,
        "version": settings.APP_VERSION,
    }