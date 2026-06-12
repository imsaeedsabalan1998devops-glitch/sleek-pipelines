.PHONY: install lint test coverage run docker coverage-html

install:
	pip install -r requirements.txt

lint:
	flake8 src tests

test:
	pytest

coverage:
	pytest --cov=src --cov-report=term-missing

coverage-html:
	pytest --cov=src --cov-report=html

run:
	python src/main.py

docker:
	docker build -t devops-playground .
