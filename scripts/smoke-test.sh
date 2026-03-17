#!/usr/bin/env bash
set -euo pipefail

base_url="${1:-http://127.0.0.1:8080}"
artifacts_dir="${2:-artifacts/smoke}"

mkdir -p "$artifacts_dir"

echo "Checking /health"
curl --fail --silent "$base_url/health" -o "$artifacts_dir/health.json"
python scripts/validate-json.py "$artifacts_dir/health.json" status ok
python scripts/validate-json.py "$artifacts_dir/health.json" service secure-docker-api

echo "Checking /ready"
curl --fail --silent "$base_url/ready" -o "$artifacts_dir/ready.json"
python scripts/validate-json.py "$artifacts_dir/ready.json" status ready

echo "Checking /version"
curl --fail --silent "$base_url/version" -o "$artifacts_dir/version.json"
python scripts/validate-json.py "$artifacts_dir/version.json" service secure-docker-api

echo "Smoke test passed for $base_url"
