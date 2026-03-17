# secure-docker-api

Secure Dockerized API with branch-based delivery flow, smoke tests, and image scanning.

## Overview

`secure-docker-api` is a small Flask service built to demonstrate an intermediate DevOps workflow from a greenfield repository. The repo focuses on practical packaging, hardening, validation, and promotion through `dev`, `main`, and `prod`. The `prod` branch is the final release-grade state with stronger promotion governance, release documentation, and ownership/security guidance.

## Architecture

- Flask API served by Gunicorn
- Multi-stage Docker build
- Non-root runtime container
- Docker Compose for local validation
- GitHub Actions for PR validation and release promotion
- Build metadata captured in image labels and `/version`

See [docs/architecture.md](docs/architecture.md) for the detailed view.

## Environment Flow

- `dev`: daily integration branch for feature work
- `main`: reviewed and stable integration branch
- `prod`: release-only branch for approved promotions from `main`

Promotion path: `feature/* -> dev -> main -> prod`

## Local Setup

1. Create and activate a Python 3.11 virtual environment.
2. Install dependencies with `pip install -r requirements-dev.txt`.
3. Run `python -m pytest` and `python -m ruff check .`.
4. Build locally with `docker build -t secure-docker-api:local .`.
5. Start the stack with `docker compose --env-file .env.dev.example up --build -d`.
6. Use `./scripts/local-validate.sh` before opening PRs into `dev`.

## Validation Steps

1. Lint the repo: `python -m ruff check .`
2. Run tests: `python -m pytest`
3. Build the image: `docker build -t secure-docker-api:local .`
4. Start the container: `docker compose --env-file .env.dev.example up --build -d`
5. Validate endpoints:
   - `curl http://127.0.0.1:8080/health`
   - `curl http://127.0.0.1:8080/ready`
   - `curl http://127.0.0.1:8080/version`
6. Run smoke script: `./scripts/smoke-test.sh` or `powershell -File .\scripts\smoke-test.ps1`
7. Review generated validation artifacts under `artifacts/`
8. Stop the stack: `docker compose down --remove-orphans`

## CI/CD Flow

PR validation on `dev` and `main` runs these stages:

1. code lint
2. unit tests
3. Docker build
4. container smoke tests
5. image scan

Promotion from `main` uses the release workflow to rerun validation, package a release artifact, and pause at the protected `prod` environment before the `main -> prod` PR merge.

The `prod` branch additionally stores:

- pytest XML reports
- smoke test JSON responses
- build metadata linked to the commit SHA
- release manifest metadata for audit and rollback

## Rollback

Rollback is documented in [docs/rollback.md](docs/rollback.md). Minimum rollback practice for this repo:

- redeploy the last known good image
- confirm `/health`, `/ready`, and `/version`
- capture rollback notes in the release PR

## Troubleshooting

Use [docs/troubleshooting.md](docs/troubleshooting.md) for common startup, readiness, and image scan failures.

See [docs/developer-workflow.md](docs/developer-workflow.md) for the branch-specific engineering workflow on `dev`.
See [docs/release-checklist.md](docs/release-checklist.md), [docs/production-promotion.md](docs/production-promotion.md), and [docs/security-notes.md](docs/security-notes.md) for the final `prod` branch operating model.

On `prod`, protected validation requires GitHub Environment approval before checks run.

## Repo Map

- `app/`: Flask application source and runtime config helpers
- `tests/`: endpoint and behavior tests
- `scripts/`: local smoke and validation helpers
- `artifacts/`: generated local validation outputs such as smoke responses and test reports
- `docs/`: architecture, release, rollback, and troubleshooting notes
- `.github/workflows/`: CI and release automation
- `.github/workflows/protected-prod-validation.yml`: manual-gated validation for the protected `prod` branch
- `.github/PULL_REQUEST_TEMPLATE.md`: PR checklist with rollback notes
- `.github/CODEOWNERS`: ownership guidance for review and release approval
- `.pre-commit-config.yaml`: optional local hooks for lint and tests
- `.env.dev.example`: local development environment example
- `.env.main.example`: stable integration environment example
- `.env.prod.example`: production-style environment example
- `Dockerfile`: multi-stage container build with non-root runtime
- `gunicorn.conf.py`: Gunicorn runtime configuration based on environment variables
- `docker-compose.yml`: local container startup and health validation
- `Makefile`: common local commands for lint, test, build, run, and cleanup
- `requirements.txt`: runtime Python dependencies
- `requirements-dev.txt`: development and test dependencies
- `pyproject.toml`: Ruff and pytest configuration
- `CHEATSHEET.md`: quick command reference
- `FILES_EXPLAINED.md`: file-by-file purpose reference
- `SECURITY.md`: vulnerability handling and secret safety notes

## Required GitHub Branch Protections

- Protect `main` and `prod`
- Require pull requests and passing status checks
- Require rollback notes in promotion PRs
- Configure `prod` environment approval in GitHub before using the release workflow
