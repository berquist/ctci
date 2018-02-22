test:
	# pytest -v ./*.py
	find . -type f -name "*.py" -exec pytest -v '{}' +

clean:
	\rm -rf __pycache__
