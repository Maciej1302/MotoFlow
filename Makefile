build:
	docker compose build

up:
	docker compose up

down:
	docker compose down

restart: down up

supercode:
	isort .
	black .
	flake8 .

test:
	python3 manage.py test

build-prod:
	docker compose -f docker-compose.prod.yml build

up-prod:
	docker compose -f docker-compose.prod.yml up

down-prod:
	docker compose -f docker-compose.prod.yml down --volumes --remove-orphans

restart-prod: down-prod up-prod

logs-prod:
	docker compose -f docker-compose.prod.yml logs -f