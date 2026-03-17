# Release Checklist

Use this checklist before merging a `main -> prod` promotion PR.

## Required checks

- PR validation workflow is green
- release-promotion workflow completed
- release manifest artifact uploaded
- rollback notes filled in the PR template
- `/health`, `/ready`, and `/version` validated against the release candidate

## Reviewer checks

- image scan has no unapproved blocking findings
- Dockerfile and workflow changes are understood
- docs changed with the release are still accurate
- version and commit metadata exposed by `/version` match the release candidate
