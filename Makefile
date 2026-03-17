PYTHON ?= python
IMAGE ?= secure-docker-api:local
COMPOSE ?= docker compose
BUILD_DATE ?= dev-build
VCS_REF ?= local

.PHONY: lint test build run down clean smoke validate scan

lint:
	$(PYTHON) -m ruff check .

test:
	$(PYTHON) -m pytest

build:
	docker build --build-arg BUILD_DATE=$(BUILD_DATE) --build-arg VCS_REF=$(VCS_REF) -t $(IMAGE) .

run:
	$(COMPOSE) --env-file .env.dev.example up --build -d

down:
	$(COMPOSE) down --remove-orphans

smoke:
	./scripts/smoke-test.sh

validate:
	./scripts/local-validate.sh

scan:
	docker run --rm -v /var/run/docker.sock:/var/run/docker.sock aquasec/trivy:latest image $(IMAGE)

clean:
	$(COMPOSE) down --remove-orphans --volumes
	docker image rm -f $(IMAGE) 2>/dev/null || true
