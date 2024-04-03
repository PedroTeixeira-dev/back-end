PROJECT_NAME := ipc-server
PYTHON_VERSION := 3.11.0
VENV_NAME := $(PROJECT_NAME)-$(PYTHON_VERSION)

up: ## up the environment in the docker-compose
	compose -f compose.yaml up -d

build: ## up the environment in the docker-compose building the image
	compose -f compose.yaml up -d --build

down: ## down the environment in the docker-compose
	compose -f compose.yaml down
	compose -f compose.yaml rm

db-upgrade:
	flask db upgrade -d ais_server/migrations

db-downgrade:
	flask db downgrade -d ais_server/migrations

create-venv: ## install python, create virtualenv and set virtualenv to current
	pyenv install -s $(PYTHON_VERSION)
	pyenv uninstall -f $(VENV_NAME)
	pyenv virtualenv $(PYTHON_VERSION) $(VENV_NAME)
	pyenv local $(VENV_NAME)
	pip install pip -U