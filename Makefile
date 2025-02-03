all: env build run

env:
	python3 -m venv .venv-ubuntu
	. .venv-ubuntu/bin/activate

build:
	.venv-ubuntu/bin/pip install pdf2docx

run:
	.venv-ubuntu/bin/python3 main.py