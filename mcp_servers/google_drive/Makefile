.PHONY: docker-build docker-rm docker rm docker-up docker-upd up upd

DOCKER_COMPOSE=docker compose

# Build the Docker image for this service
docker-build:
	$(DOCKER_COMPOSE) build --no-cache

docker: docker-build

# Run the Docker container for this service
docker-up:
	$(DOCKER_COMPOSE) up

docker-upd:
	$(DOCKER_COMPOSE) up -d

down:
	$(DOCKER_COMPOSE) down

up: docker-up

upd: docker-upd

# Remove the Docker image using the script
docker-rm:
	./remove_gdrive_image.sh

rm: docker-rm 