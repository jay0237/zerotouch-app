from fastapi import FastAPI

from app.api.v1.root import router as root_router
from app.api.v1.health import router as health_router
from app.api.v1.version import router as version_router

app = FastAPI(
    title="ZeroTouch",
    description="ZeroTouch GitOps Deployment Platform",
    version="0.1.0",
)

app.include_router(root_router)
app.include_router(health_router)
app.include_router(version_router)