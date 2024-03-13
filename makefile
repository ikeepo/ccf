PWD = $(shell pwd)
black:
	docker-compose exec web black .
pytest:
	docker-compose exec web pytest .
docker_p:
	docker-compose exec web-db psql -U postgres
routine: 
	docker-compose exec web flake8 .
	docker-compose exec web black .
	docker-compose exec web isort .
	docker-compose exec web pytest .
rebuild:
	docker-compose up -d --build
init_venv:
	python -m venv .venv
	source $(PWD)/.venv/bin/activate && \
    python -m pip install -r requirements.txt
init_db_meta:
	docker-compose exec web aerich init -t app.db.TORTOISE_ORM
init_db:
	docker-compose exec web aerich init-db