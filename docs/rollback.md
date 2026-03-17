# Rollback

## Goal

Restore the last known good container release if a new image fails health, readiness, or smoke validation.

## Rollback steps

1. Identify the last approved image tag or commit from `main`.
2. Stop the failing container deployment.
3. Redeploy the previous image tag with the prior environment file.
4. Confirm `/health`, `/ready`, and `/version` return expected responses.
5. Record the incident, cause, and follow-up fix before the next promotion.

## Common rollback triggers

- Container fails Docker healthcheck
- `/ready` returns non-ready during release validation
- Trivy reports a blocking high or critical issue
- Smoke test fails after image rebuild

## Minimum rollback evidence

- image tag or commit hash restored
- timestamp of rollback
- validation output after rollback
