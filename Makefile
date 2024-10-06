ifneq ("$(wildcard .env)","")
	include .env
	export
endif

.PHONY: install
install: ## Install Python requirements.
	python -m pip install --upgrade pip setuptools wheel poetry
	poetry lock
	poetry install --no-root
	poetry run pre-commit install

.PHONY: treinot
treinot: ## Run the project.
	poetry run python -m src.app --modo TREINOT

.PHONY: treinop
treinop: ## Run the project.
	poetry run python -m src.app --modo TREINOP

.PHONY: video
video: ## Run the project.
	poetry run python -m src.app --modo VIDEO

.PHONY: run-transform-positive
run-transform-positive: ## Run first example script.
	poetry run python src/scripts/transform_image_positive.py

.PHONY: run-transform-negative
run-transform-negative: ## Run environment variables usage example script.
	poetry run python src/scripts/transform_image_negative.py

.DEFAULT_GOAL := help
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sed 's/Makefile://g' | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
