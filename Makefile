PYTHON ?= python
IMAGE ?= secure-docker-api:local
COMPOSE ?= docker compose

.PHONY: lint test build run down clean smoke

lint:
	$(PYTHON) -m ruff check .

test:
	$(PYTHON) -m pytest

build:
	docker build -t $(IMAGE) .

run:
	$(COMPOSE) --env-file .env.dev.example up --build -d

down:
	$(COMPOSE) down --remove-orphans

smoke:
	./scripts/smoke-test.sh

clean:
	$(COMPOSE) down --remove-orphans --volumes
	docker image rm -f $(IMAGE) 2>/dev/null || true
