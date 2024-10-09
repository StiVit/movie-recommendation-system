# Makefile

.PHONY: all venv activate install_env copy_env

all: venv activate install_env copy_env

venv:
	python -m venv .venv

activate:
	@echo "To activate the virtual environment, run:"
	@echo "source .venv/bin/activate"  # On Windows, use `.venv\Scripts\activate`

install_env: venv
	venv/bin/pip install -r requirements.txt  # On Windows, use `venv\Scripts\pip install -r requirements.txt`