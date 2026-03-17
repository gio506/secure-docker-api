"""Flask entrypoint for secure-docker-api."""

from __future__ import annotations

from flask import Flask, jsonify

from app.config import get_settings

app = Flask(__name__)


@app.get("/health")
def health() -> tuple[dict[str, str], int]:
    settings = get_settings()
    return jsonify({"status": "ok", "service": settings["app_name"]}), 200


@app.get("/ready")
def ready() -> tuple[dict[str, str], int]:
    settings = get_settings()
    state = settings["ready_state"]
    status_code = 200 if state == "ready" else 503
    return jsonify({"status": state, "service": settings["app_name"]}), status_code


@app.get("/version")
def version() -> tuple[dict[str, str], int]:
    settings = get_settings()
    return (
        jsonify(
            {
                "service": settings["app_name"],
                "environment": settings["app_env"],
                "version": settings["app_version"],
                "commit_sha": settings["app_commit_sha"],
            }
        ),
        200,
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=False)
