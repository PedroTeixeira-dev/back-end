PROJECT_NAME := ipc_app
PYTHON_VERSION := 3.11.0
VENV_NAME := $(PROJECT_NAME)-$(PYTHON_VERSION)

up: ## up the environment in the docker-compose
	docker-compose up -d

build: ## up the environment in the docker-compose building the image
	docker-compose up -d --build

down: ## down the environment in the docker-compose
	docker-compose down
	docker-compose rm

db-upgrade:
	flask db upgrade -d ipc_app/migrations

db-downgrade:
	flask db downgrade -d ipc_app/migrations

create-venv: ## install python, create virtualenv and set virtualenv to current
	pyenv install -s $(PYTHON_VERSION)
	pyenv uninstall -f $(VENV_NAME)
	pyenv virtualenv $(PYTHON_VERSION) $(VENV_NAME)
	pyenv local $(VENV_NAME)
	pip3 install -U pip pipenv


setup-dev: ## install dev requirements
	pipenv install --deploy --dev

setup: ## install requirements
	pipenv install --deploy

logs: ## project logs on container
	docker logs $(PROJECT_NAME) --follow

sh: ## run sh inside container
	docker exec -it $(PROJECT_NAME) sh
