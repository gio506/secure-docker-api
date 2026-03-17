#!/usr/bin/env bash
set -euo pipefail

cleanup() {
  docker compose down --remove-orphans >/dev/null 2>&1 || true
}

trap cleanup EXIT

mkdir -p artifacts

python -m ruff check .
python -m pytest --junitxml artifacts/pytest-report.xml
docker build \
  --build-arg BUILD_DATE="$(date -u +"%Y-%m-%dT%H:%M:%SZ")" \
  --build-arg VCS_REF="${GIT_COMMIT:-local}" \
  -t secure-docker-api:local .
docker compose --env-file .env.dev.example up --build -d
./scripts/smoke-test.sh
