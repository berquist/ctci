.PHONY: test
test:
	# pytest -v ./*.py
	find . -type f -name "*.py" -exec pytest -v '{}' +

.PHONY: clean
clean:
	find . -type f -name "*.html" -exec rm -f '{}' +
	find . -type f -name "*.pyc" -exec rm -f '{}' +
