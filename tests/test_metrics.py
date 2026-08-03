from fastapi.testclient import TestClient

from app.main import app


def test_metrics_endpoint_exposes_prometheus_metrics() -> None:
    @app.get("/__test__/boom")
    def boom() -> None:
        raise RuntimeError("boom")

    client = TestClient(app, raise_server_exceptions=False)

    assert client.get("/api/v1/health").status_code == 200
    assert client.get("/__test__/boom").status_code == 500

    response = client.get("/metrics")

    assert response.status_code == 200
    body = response.text

    assert "http_requests_total" in body
    assert "http_request_duration_seconds" in body
    assert "http_request_size_bytes" in body
    assert "http_response_size_bytes" in body
    assert "http_requests_inprogress" in body
    assert "app_exceptions_total" in body
    assert "process_cpu_seconds_total" in body
    assert "python_gc_objects_collected_total" in body