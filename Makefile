all: init docs test

init:
	pip install tox coverage Sphinx twine

test:
	coverage erase
	tox -p
	coverage html

fast_test:
	coverage run runtests.py
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
