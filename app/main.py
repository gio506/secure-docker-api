"""Flask entrypoint for secure-docker-api."""

from __future__ import annotations

from flask import Flask, jsonify

from app.config import get_settings


def create_app() -> Flask:
    app = Flask(__name__)

    @app.get("/health")
    def health() -> tuple[dict[str, str], int]:
        settings = get_settings()
        return jsonify({"status": "ok", "service": settings.app_name}), 200

    @app.get("/ready")
    def ready() -> tuple[dict[str, str], int]:
        settings = get_settings()
        status_code = 200 if settings.ready_state == "ready" else 503
        return jsonify({"status": settings.ready_state, "service": settings.app_name}), status_code

    @app.get("/version")
    def version() -> tuple[dict[str, str], int]:
        settings = get_settings()
        return (
            jsonify(
                {
                    "service": settings.app_name,
                    "environment": settings.app_env,
                    "version": settings.app_version,
                }
            ),
            200,
        )

    return app


app = create_app()


if __name__ == "__main__":
    settings = get_settings()
    app.run(host=settings.app_host, port=settings.app_port, debug=False)
