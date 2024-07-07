run:
	@uvicorn restaurante.main:app --reload

db:
	@docker-compose up -d

stop-db:
	@docker-compose down

stop-postgres:
	@sudo systemctl stop postgresql

create-migrations:
	@PYTHONPATH=$PYTHONPATH:$(pwd) alembic revision --autogenerate -m $(name)

run-migrations:
	@PYTHONPATH=$PYTHONPATH:$(pwd) alembic upgrade head