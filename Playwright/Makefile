.PHONY: test test-ui test-headed test-debug install

install:
	pip install pytest pytest-playwright
	playwright install

test:
	pytest

test-headed:
	pytest --headed

test-debug:
	pytest --headed --slowmo 1000

test-watch:
	pytest-watch  # requires pytest-watch package