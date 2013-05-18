all: init docs test

init:
	python setup.py develop
	pip install tox coverage Sphinx

test:
	coverage erase
	tox
	coverage html

fast_test:
	coverage run setup.py test
	coverage report
	coverage html

docs: documentation

documentation:
	python setup.py build_sphinx
