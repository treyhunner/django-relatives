all: init docs test

init:
	python setup.py develop
	pip install tox coverage Sphinx twine

test:
	coverage erase
	tox
	coverage html

fast_test:
	coverage run setup.py test
	coverage report
	coverage html

create:
	python setup.py sdist bdist_wheel
	twine check dist/*

test_upload:
	twine upload --repository-url https://test.pypi.org/legacy/ dist/*

upload:
	twine upload dist/*

docs: documentation

documentation:
	python setup.py build_sphinx
