#!/usr/bin/env bash
set -euo pipefail

base_url="${1:-http://127.0.0.1:8080}"

echo "Checking /health"
curl --fail --silent "$base_url/health" >/dev/null

echo "Checking /ready"
curl --fail --silent "$base_url/ready" >/dev/null

echo "Checking /version"
curl --fail --silent "$base_url/version" >/dev/null

echo "Smoke test passed for $base_url"
