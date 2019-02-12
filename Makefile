default: help

help:
	@echo "Usage:"
	@echo
	@echo "	make help		Print this help message"
	@echo "	make clean		Cleanup build directories"
	@echo "	make dist		Create and publish PYPI package"
	@echo "	make init-dev		Initialize development environment"

clean:
	rm -rf dist/ || true && rm -rf *.egg-info || true

dist:
	python3 setup.py sdist

init-dev:
	sudo pip3 install -r dev-requirements.txt
	scripts/init-development.py
