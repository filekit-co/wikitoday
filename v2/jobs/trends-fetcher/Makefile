SHELL := /bin/bash

.PHONY: init run compile_proto

init:
	@python3 -m venv venv && source venv/bin/activate && pip install --upgrade pip

run:
	@export PYTHONPATH=$$PYTHONPATH:/Users/minwook/code/filekit/wikitoday/v2/libs/python:/Users/minwook/code/filekit/wikitoday/v2/libs/protobuf && \
	source venv/bin/activate && \
	python main.py
