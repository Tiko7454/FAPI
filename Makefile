PG_USER := postgres
PG_PASSWORD := pass123
DB_NAME := fapi
DB_HOST := localhost

help:
	@echo "run server: make run"
	@echo "install dependencies: make deps"
	@echo "perform migrations: make migrate"
	@echo "create db: make create_db"
	@echo "drop db: make drop_db"

run:
	uvicorn main:app --reload

deps: requirements.txt
	pip-sync

requirements.txt: requirements.in
	pip-compile

migrate:
	alembic upgrade head

create_db:
	@PGPASSWORD=$(PG_PASSWORD) createdb -h ${DB_HOST} -U ${PG_USER} ${DB_NAME}
	@PGPASSWORD=$(PG_PASSWORD) psql -h localhost -U $(PG_USER) -c "ALTER DATABASE $(DB_NAME) OWNER TO $(PG_USER);"
	@alembic revision --autogenerate -m "Init"

drop_db:
	@PGPASSWORD=$(PG_PASSWORD) psql -h localhost -U $(PG_USER) -c "DROP DATABASE IF EXISTS $(DB_NAME);"
