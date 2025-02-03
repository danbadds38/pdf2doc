all: check env build run

check:
	@which python3 > /dev/null || sudo apt-get update && sudo apt-get install -y python3 python3-pip python3-venv && python3 --version

env:
	python3 -m venv .venv-ubuntu
	. .venv-ubuntu/bin/activate

build:
	.venv-ubuntu/bin/pip install pdf2docx

run:
	.venv-ubuntu/bin/python3 main.py