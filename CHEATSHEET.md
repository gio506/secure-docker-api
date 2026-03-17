# Cheatsheet

## Python setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
```

## Local validation

```bash
python -m ruff check .
python -m pytest
docker build -t secure-docker-api:local .
docker compose --env-file .env.dev.example up --build -d
./scripts/smoke-test.sh
docker compose down --remove-orphans
```

## Windows smoke test

```powershell
powershell -File .\scripts\smoke-test.ps1
```

## Make targets

```bash
make lint
make test
make build
make run
make down
make clean
```

## Branch flow

```text
feature/* -> dev -> main -> prod
```
