test:
	# pytest -v ./*.py
	find . -type f -name "*.py" -exec pytest -v '{}' +

clean:
	find . -type f -name "*.pyc" -exec rm -f '{}' +
