# Changelog

All notable changes to this project are documented in this file.
Format follows [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## [Unreleased]

### Changed
- Migrated Trivy image scanning to official `aquasecurity/trivy-action@0.31.0` in all five workflows
- Added `ruff format --check` stage alongside `ruff check` for consistent code style enforcement
- Added `cache: "pip"` to all `actions/setup-python` steps to speed up CI dependency installation
- Added `docker/setup-buildx-action@v3` to all docker-build jobs for layer caching and multi-platform support
- Added `--volumes` flag to `docker compose down` teardown steps to prevent volume leakage between runs
- Added `retention-days: 7` and `if-no-files-found: ignore` to artifact upload steps
- Added `security-events: write` permission to all `image-scan` jobs for future SARIF upload support
- Added `workflow_dispatch` trigger to `dev-validation.yml` for manual runs

## [0.1.0] — 2026-03-17

### Added
- Initial release: Flask API with `/health`, `/ready`, `/version` endpoints
- Multi-stage Dockerfile with non-root `appuser`, OCI labels, and HEALTHCHECK
- Five-workflow GitHub Actions pipeline (dev, pr, main, prod, release-promotion)
- Trivy container image scanning on every branch
- Pre-commit config with ruff, shellcheck, and trailing-whitespace hooks
- Branch-based environment delivery (dev → main → prod)
- CODEOWNERS, PR template, and environment approval gates
