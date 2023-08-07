.PHONY: dev

# uvicorn only warning error log
dev:
	export PYTHONPATH=${PYTHONPATH}:./src && poetry run uvicorn main:app --reload --log-level warning

test:
	export PYTHONPATH=${PYTHONPATH}:./src && poetry run pytest