test:
	pytest -v --cov=src ./tests
cov:
	py.test --cov-report html --cov=src ./tests
lint:
	ruff check --fix ./src
	ruff check --fix ./tests