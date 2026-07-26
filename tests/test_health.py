from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

def test_health():
    response = client.get("/api/v1/health")
    
    assert response.status_code == 200
    assert response.json() ["status"] == "healthy"


def test_live():
    response = client.get("/api/v1/live")
    
    assert response.status_code == 200
    assert response.json() ["status"] == "alive"


def test_ready():
    response = client.get("/api/v1/ready")
    
    assert response.status_code == 200
    assert response.json() ["status"] == "ready"