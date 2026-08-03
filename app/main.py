from fastapi import FastAPI, Request
from prometheus_client import Counter
from prometheus_fastapi_instrumentator import Instrumentator

from app.api.v1.health import router as health_router
from app.api.v1.root import router as root_router
from app.api.v1.version import router as version_router
from app.core.logging import setup_logging
from app.core.settings import settings

setup_logging()

import logging

logger = logging.getLogger(__name__)
logger.info("Starting %s v%s", settings.APP_NAME, settings.APP_VERSION)
app = FastAPI(
    title=settings.APP_NAME,
    description="Production-ready GitOps Deployment Platform",
    version=settings.APP_VERSION,
)

app_exceptions_total = Counter(
    "app_exceptions_total",
    "Total number of unhandled application exceptions.",
    ["exception"],
)


@app.middleware("http")
async def record_unhandled_exceptions(request: Request, call_next):
    try:
        return await call_next(request)
    except Exception as exc:
        app_exceptions_total.labels(type(exc).__name__).inc()
        raise

app.include_router(root_router, prefix="/api/v1", tags=["Root"])
app.include_router(health_router, prefix="/api/v1", tags=["Health"])
app.include_router(version_router, prefix="/api/v1", tags=["Version"])

Instrumentator(
    should_instrument_requests_inprogress=True,
    excluded_handlers=["/metrics"],
).instrument(app).expose(app)