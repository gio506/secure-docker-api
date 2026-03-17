from __future__ import annotations

import os


def test_health_endpoint(client):
    response = client.get("/health")

    assert response.status_code == 200
    assert response.get_json()["status"] == "ok"


def test_ready_endpoint_when_ready(client, monkeypatch):
    monkeypatch.setenv("READY_STATE", "ready")

    response = client.get("/ready")

    assert response.status_code == 200
    assert response.get_json()["status"] == "ready"


def test_ready_endpoint_when_not_ready(client, monkeypatch):
    monkeypatch.setenv("READY_STATE", "warming")

    response = client.get("/ready")

    assert response.status_code == 503
    assert response.get_json()["status"] == "warming"


def test_version_endpoint_returns_env_and_version(client, monkeypatch):
    monkeypatch.setenv("APP_ENV", "main")
    monkeypatch.setenv("APP_VERSION", "1.2.3")

    response = client.get("/version")
    payload = response.get_json()

    assert response.status_code == 200
    assert payload["environment"] == "main"
    assert payload["version"] == "1.2.3"
    assert payload["service"] == "secure-docker-api"


def test_default_env_is_dev(client):
    os.environ.pop("APP_ENV", None)
    os.environ.pop("APP_VERSION", None)

    response = client.get("/version")
    payload = response.get_json()

    assert payload["environment"] == "dev"
    assert payload["version"] == "0.1.0"
