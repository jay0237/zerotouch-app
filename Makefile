IMAGE_NAME=zerotouch
CONTAINER_NAME=zerotouch-app

build:
	docker build -t $(IMAGE_NAME):latest .

run:
	docker run --rm -p 8000:8000 --name $(CONTAINER_NAME) $(IMAGE_NAME):latest

test:
	poetry run pytest

lint:
	poetry run ruff check .

format:
	poetry run ruff format .

clean:
	docker image rm -f $(IMAGE_NAME):latest || true