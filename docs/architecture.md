# Architecture

`secure-docker-api` is a small Flask service packaged for Docker-first delivery. The application exposes:

- `/health` for container and service liveliness
- `/ready` for release readiness signaling
- `/version` for environment and version visibility

## Components

- Flask app for a minimal HTTP surface
- Gunicorn for production-style process serving
- Docker multi-stage build for smaller runtime images
- Docker Compose for local validation
- GitHub Actions for branch-aware CI and release promotion

## Environment flow

- `dev`: feature integration and first PR validation target
- `main`: stable integration branch after review and checks
- `prod`: release-only branch reached from `main` after approval

## Runtime settings

- `APP_ENV` controls the reported environment name
- `APP_VERSION` controls the `/version` response
- `READY_STATE` allows readiness simulation for validation and troubleshooting
