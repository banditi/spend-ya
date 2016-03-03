.PHONY: all
all: start

.PHONY: start
start:
	. ./tools/scripts/setup.sh

.PHONY: validate
validate: lint test

.PHONY: lint
lint:
	echo "Linting via PEP8"
	pep8

.PHONY: test
test:
	echo "Testing"
	python manage.py test

.PHONY: pip
pip:
	pip install -r requirements.txt

.PHONY: dev
dev:
	python manage.py runserver 5000
