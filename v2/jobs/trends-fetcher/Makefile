.PHONY: init freeze run compile_proto

SHELL := /bin/bash
LIB_PATH := ../../libs
PYTHON_LIB_PATH := $(LIB_PATH)/python
PROTOBUF_LIB_PATH := $(LIB_PATH)/protobuf


init:
	@python3 -m venv venv && source venv/bin/activate && pip install --upgrade pip


compile_proto:
	@protoc -I=$(PROTOBUF_LIB_PATH) --python_out=$(PROTOBUF_LIB_PATH) $(PROTOBUF_LIB_PATH)/*.proto


run: compile_proto
	@export PYTHONPATH=$$PYTHONPATH:$(PYTHON_LIB_PATH):$(PROTOBUF_LIB_PATH) && \
	source venv/bin/activate && \
	python main.py

freeze:
	@source venv/bin/activate && \
	pip freeze > requirements.txt

prepare:
	@rm -rf ./cp_libs
	@mkdir -p ./cp_libs/protobuf ./cp_libs/python
	@cp -r $(PYTHON_LIB_PATH)/* ./cp_libs/python
	@cp $(PROTOBUF_LIB_PATH)/*.py ./cp_libs/protobuf


deploy: freeze compile_proto prepare
	@export PROJECT_ID=poetic-producer-396107 && \
	gcloud builds submit --config deploy.cloudbuild.yaml
