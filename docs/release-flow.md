# Release Flow

## Branch promotion model

1. Create `feature/*` branches from `dev`.
2. Open a PR into `dev` and require the PR validation workflow to pass.
3. Promote validated changes from `dev` to `main` by PR.
4. Review rollback notes before opening the promotion PR from `main` to `prod`.
5. Use GitHub environment protection for `prod` to require manual approval.

## Required GitHub settings

- Protect `main` and `prod`
- Require pull requests before merge
- Require status checks:
  - `lint`
  - `unit-tests`
  - `docker-build`
  - `container-smoke-tests`
  - `image-scan`
- Require rollback notes in the PR description for `main` and `prod` promotions
- Configure `prod` as a protected environment with approvers

## Release notes

- Keep release notes short and practical
- Include version, risk, rollback action, and validation results
- Prefer action-based commit subjects such as `Harden Docker runtime`
