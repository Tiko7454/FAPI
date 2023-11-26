PG_USER := postgres
PG_PASSWORD := pass123
DB_NAME := fapi
DB_HOST := localhost

help:
	@echo "run server: make run"
	@echo "install dependencies: make deps"
	@echo "perform migrations: make migrate"

run:
	uvicorn main:app --reload

deps: requirements.txt
	pip-sync

requirements.txt: requirements.in
	pip-compile

migrate: drop_db create_db

create_db:
	@PGPASSWORD=$(PG_PASSWORD) createdb -h ${DB_HOST} -U ${PG_USER} ${DB_NAME}
	@PGPASSWORD=$(PG_PASSWORD) psql -h localhost -U $(PG_USER) -c "ALTER DATABASE $(DB_NAME) OWNER TO $(PG_USER);"

drop_db:
	@PGPASSWORD=$(PG_PASSWORD) psql -h localhost -U $(PG_USER) -c "DROP DATABASE IF EXISTS $(DB_NAME);"
