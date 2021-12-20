install: requirements.txt
	pip install -r requirements.txt

start:
	python api/main.py

format:
	yapf --recursive --in-place api

lint:
	flake8 api
