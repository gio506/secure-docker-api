# Branch Differences

This repository uses three long-lived branches with increasing maturity:

- `main`: stable baseline
- `dev`: stronger engineering workflow
- `prod`: release-grade controls

## Summary Table

| Branch | Purpose | Pipeline behavior | Main additions |
|---|---|---|---|
| `main` | stable baseline branch | approval-gated validation for `main` | safe runtime config, app factory, Gunicorn config |
| `dev` | daily engineering and integration | automatic validation on push to `dev` and PRs to `dev`/`main` | stronger validation, artifacts, commit metadata, developer workflow |
| `prod` | release-only branch | approval-gated validation for `prod` plus release workflow | release governance, manifest generation, security and ownership docs |

## `main` vs `dev`

`dev` includes everything from `main`, plus these additional files or changes:

- `.github/workflows/pr-validation.yml`
- `Dockerfile`
- `README.md`
- `app/config.py`
- `app/main.py`
- `gunicorn.conf.py`
- `tests/conftest.py`
- `tests/test_api.py`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.pre-commit-config.yaml`
- `docs/developer-workflow.md`
- `scripts/local-validate.sh`
- `scripts/smoke-test.sh`
- `scripts/validate-json.py`

### Practical difference

- `main` is the safer baseline with protected validation
- `dev` adds automatic validation on push, smoke artifacts, JSON response checks, and commit metadata in `/version`

## `dev` vs `prod`

`prod` includes everything from `dev`, plus these additional files or changes:

- `.github/CODEOWNERS`
- `.github/workflows/protected-prod-validation.yml`
- `.github/workflows/release-promotion.yml`
- `README.md`
- `FILES_EXPLAINED.md`
- `SECURITY.md`
- `docs/production-promotion.md`
- `docs/release-checklist.md`
- `docs/security-notes.md`
- `scripts/create-release-manifest.py`

### Practical difference

- `dev` is optimized for engineering flow
- `prod` is optimized for controlled release flow, approvals, rollback evidence, and release artifacts

## Pipeline Behavior

| Branch | Trigger style |
|---|---|
| `dev` | `dev-validation.yml` runs automatically on push and PRs to `dev` |
| `main` | `protected-main-validation.yml` requires approval through the protected `main` environment before checks start |
| `prod` | `protected-prod-validation.yml` requires approval through the protected `prod` environment before checks start |

## Recommended Promotion Path

```text
feature/* -> dev -> main -> prod
```
