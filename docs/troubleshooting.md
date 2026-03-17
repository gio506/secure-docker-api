# Troubleshooting

## Container does not start

- Check `docker compose logs`
- Confirm port `8080` is free
- Rebuild with `docker compose build --no-cache`
- Verify the runtime image still includes Gunicorn and Flask dependencies

## Healthcheck fails

- Inspect container health with `docker inspect secure-docker-api`
- Query `http://127.0.0.1:8080/health` directly
- Confirm the service is listening on `0.0.0.0:8080`

## Readiness fails

- Review `READY_STATE` in the active env file
- Use `READY_STATE=ready` for normal local validation
- If testing failure handling, expect `/ready` to return HTTP 503

## Image scan fails

- Review the Trivy output for package and severity details
- Rebuild the image after dependency updates
- Do not promote to `main` or `prod` until blocking findings are addressed or consciously accepted outside this lab
