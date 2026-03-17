#!/usr/bin/env bash
set -euo pipefail

cleanup() {
  docker compose down --remove-orphans >/dev/null 2>&1 || true
}

trap cleanup EXIT

python -m ruff check .
python -m pytest
docker build -t secure-docker-api:local .
docker compose --env-file .env.dev.example up --build -d
./scripts/smoke-test.sh
