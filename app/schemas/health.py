from pydantic import BaseModel


class HealthResponse(BaseModel):
    status: str
    service: str


class LiveResponse(BaseModel):
    status: str


class ReadyResponse(BaseModel):
    status: str