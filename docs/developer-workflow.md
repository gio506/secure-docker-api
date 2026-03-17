# Developer Workflow

## Daily flow

1. Create a `feature/*` branch from `dev`.
2. Install dependencies and run local checks.
3. Use `./scripts/local-validate.sh` before opening a PR.
4. Open the PR into `dev` with rollback notes.
5. Promote `dev` to `main` only after smoke artifacts and image scan results are reviewed.

## Local shortcuts

- `make lint` for style checks
- `make test` for unit tests
- `make build` for local image build
- `make run` to boot the stack
- `make smoke` to validate running endpoints
- `make validate` for the full local flow

## What improved on dev

- smoke tests now validate payload contents
- container builds now record revision metadata
- CI stores test and smoke artifacts for review
- PRs use a standard rollback-focused template
