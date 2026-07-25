from fastapi import FastAPI

from app.core.settings import settings

from app.api.v1.root import router as root_router
from app.api.v1.health import router as health_router
from app.api.v1.version import router as version_router
from app.core.logging import setup_logging

setup_logging()

import logging
logger = logging.getLogger(__name__)
logger.info("Starting %s v%s", settings.APP_NAME, settings.APP_VERSION)
app = FastAPI(
    title=settings.APP_NAME,
    description="Production-ready GitOps Deployment Platform",
    version=settings.APP_VERSION,
)

app.include_router(root_router, prefix="/api/v1", tags=["Root"])
app.include_router(health_router, prefix="/api/v1", tags=["Health"])
app.include_router(version_router, prefix="/api/v1", tags=["Version"])