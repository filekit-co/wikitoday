.PHONY: dev

dev:
	export PYTHONPATH=${PYTHONPATH}:./src && poetry run uvicorn main:app --reload
