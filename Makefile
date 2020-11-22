all: ci

lint:
	flake8

checkformat:
	black --check .
	isort --check .

format:
	black .
	isort .

test:
	cd backend/ && pytest

migrate:
	cd backend/ && alembic upgrade head

rollback:
	cd backend/ && alembic downgrade -1

migration:
	cd backend/ && alembic revision --autogenerate -m "${MESSAGE}"

ci: checkformat lint test