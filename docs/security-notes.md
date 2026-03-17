# Security Notes

## Image scanning

- treat high and critical Trivy findings as blocking by default
- document any conscious exceptions outside the repo in the release PR
- rebuild the image after dependency updates rather than bypassing the scan

## Secrets hygiene

- keep real secrets out of the repository
- use `.env.*.example` only for placeholders and safe defaults
- do not place credentials in workflow YAML or Docker build args

## Release evidence

- keep the uploaded release manifest with the build artifacts
- link the manifest and rollback notes in every `main -> prod` promotion PR
