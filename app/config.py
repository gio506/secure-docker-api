"""Application configuration helpers."""

from __future__ import annotations

import os
from dataclasses import dataclass

ALLOWED_ENVS = {"dev", "main", "prod"}


@dataclass(frozen=True)
class Settings:
    app_name: str
    app_env: str
    app_version: str
    ready_state: str
    app_host: str
    app_port: int
    app_commit_sha: str


def _validated_env_name() -> str:
    env_name = os.getenv("APP_ENV", "dev").strip().lower()
    return env_name if env_name in ALLOWED_ENVS else "dev"


def _validated_port() -> int:
    raw_port = os.getenv("APP_PORT", "8080").strip()
    try:
        port = int(raw_port)
    except ValueError:
        return 8080
    return port if 1 <= port <= 65535 else 8080


def get_settings() -> Settings:
    """Return runtime settings from the environment."""
    return Settings(
        app_name="secure-docker-api",
        app_env=_validated_env_name(),
        app_version=os.getenv("APP_VERSION", "0.1.0").strip() or "0.1.0",
        ready_state=os.getenv("READY_STATE", "ready").strip() or "ready",
        app_host=os.getenv("APP_HOST", "0.0.0.0").strip() or "0.0.0.0",
        app_port=_validated_port(),
        app_commit_sha=os.getenv("APP_COMMIT_SHA", "local").strip() or "local",
    )
