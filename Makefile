.PHONY: venv test clean lint format ci-tests

venv:
	python -m venv .venv
	. .venv/bin/activate && pip install -r requirements.txt

test: venv
	.venv/bin/pytest --cov=quackdoor --cov-report=term-missing --cov-report=xml

clean:
	rm -rf .venv

lint: venv
	.venv/bin/black --check . && .venv/bin/mypy quackdoor && .venv/bin/pylint quackdoor

format: venv
	.venv/bin/black .

ci-tests: venv lint test