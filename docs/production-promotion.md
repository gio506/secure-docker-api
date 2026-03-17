# Production Promotion

## Goal

Keep `prod` as a release-only branch that reflects approved state from `main`.

## Promotion rules

1. Never develop directly on `prod`.
2. Open a PR from `main` to `prod`.
3. Require at least one reviewer named in `CODEOWNERS`.
4. Require rollback notes and a link to the release manifest artifact.
5. Approve the protected `prod` environment before any manual release action.

## GitHub settings to configure

- protected branch rules for `prod`
- required status checks from PR validation
- protected environment named `prod`
- reviewer approval for deployment jobs
