build:
	docker-compose build
up:
	docker-compose up
restart:
	make build
	make up

down:
	docker-compose down
