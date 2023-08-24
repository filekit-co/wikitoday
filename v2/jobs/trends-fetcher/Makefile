SHELL := /bin/bash

.PHONY: init run 

init:
	@python3 -m venv .venv && @source .venv/bin/activate && pip install --upgrade pip

run:
	@source .venv/bin/activate && python main.py
	