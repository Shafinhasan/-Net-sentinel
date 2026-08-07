from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_dashboard_is_available() -> None:
    response = client.get("/")
    assert response.status_code == 200
    assert "NetSentinel" in response.text


def test_health_endpoint() -> None:
    response = client.get("/health")
    payload = response.json()

    assert response.status_code == 200
    assert payload["status"] == "ok"
    assert payload["service"]


def test_alert_endpoint_returns_expected_shape() -> None:
    response = client.get("/api/v1/alerts?limit=10")
    payload = response.json()

    assert response.status_code == 200
    assert payload["count"] >= 0
    assert isinstance(payload["items"], list)
