PYTHON    ?= python
IMAGE     ?= secure-docker-api:local
COMPOSE   ?= docker compose
BUILD_DATE ?= $(shell date -u +'%Y-%m-%dT%H:%M:%SZ')
VCS_REF   ?= $(shell git rev-parse --short HEAD 2>/dev/null || echo local)
APP_ENV   ?= dev
APP_VERSION ?= 0.1.0-dev

.PHONY: help lint format test build run down clean smoke validate scan

help:
	@echo "Usage: make <target>"
	@echo ""
	@echo "  lint      — ruff linter check"
	@echo "  format    — ruff formatter (auto-fix)"
	@echo "  test      — run pytest suite"
	@echo "  build     — build Docker image (IMAGE=$(IMAGE))"
	@echo "  run       — start stack via docker compose (dev env)"
	@echo "  smoke     — run smoke tests against running stack"
	@echo "  validate  — run local validation script"
	@echo "  scan      — Trivy vulnerability scan on built image"
	@echo "  down      — stop stack (keep volumes)"
	@echo "  clean     — stop stack and remove volumes + image"

lint:
	$(PYTHON) -m ruff check .

format:
	$(PYTHON) -m ruff format .

test:
	$(PYTHON) -m pytest --tb=short -q

build:
	docker build \
		--build-arg BUILD_DATE="$(BUILD_DATE)" \
		--build-arg VCS_REF="$(VCS_REF)" \
		--build-arg APP_ENV="$(APP_ENV)" \
		--build-arg APP_VERSION="$(APP_VERSION)" \
		-t $(IMAGE) .

run:
	$(COMPOSE) --env-file .env.dev.example up --build -d

down:
	$(COMPOSE) down --remove-orphans

smoke:
	./scripts/smoke-test.sh

validate:
	./scripts/local-validate.sh

scan: build
	docker run --rm \
		-v /var/run/docker.sock:/var/run/docker.sock \
		aquasec/trivy:latest \
		image --severity HIGH,CRITICAL --ignore-unfixed $(IMAGE)

clean:
	$(COMPOSE) down --remove-orphans --volumes
	docker image rm -f $(IMAGE) 2>/dev/null || true
