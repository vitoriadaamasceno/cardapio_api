run:
	@uvicorn restaurante.main:app --reload

db:
	@docker-compose up -d

install:
	@pip install -r requirements.txt

stop-db:
	@docker-compose down

create-migrations:
	@PYTHONPATH=$PYTHONPATH:$(pwd) alembic revision --autogenerate -m $(name)

run-migrations:
	@PYTHONPATH=$PYTHONPATH:$(pwd) alembic upgrade head