"""Application configuration helpers."""

from __future__ import annotations

import os


def get_settings() -> dict[str, str]:
    """Return runtime settings from the environment."""
    return {
        "app_name": "secure-docker-api",
        "app_env": os.getenv("APP_ENV", "dev"),
        "app_version": os.getenv("APP_VERSION", "0.1.0"),
        "ready_state": os.getenv("READY_STATE", "ready"),
        "app_commit_sha": os.getenv("APP_COMMIT_SHA", "local"),
    }
