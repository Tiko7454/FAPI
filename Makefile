PG_USER := postgres
PG_PASSWORD := pass123
DB_NAME := fapi

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

migrate:
	@PGPASSWORD=$(PG_PASSWORD) psql -h localhost -U $(PG_USER) -c "DROP DATABASE IF EXISTS $(DB_NAME);"
	@PGPASSWORD=$(PG_PASSWORD) psql -h localhost -U $(PG_USER) -c "CREATE DATABASE $(DB_NAME);"
