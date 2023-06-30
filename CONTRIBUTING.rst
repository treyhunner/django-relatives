Contributing
============

Pull Requests
-------------

When creating a pull request, try to:

- Write tests if applicable
- Note important changes in the `CHANGES`_ file
- Update the `README`_ file if needed
- Update the documentation if needed
- Add yourself to the `AUTHORS`_ file

.. _AUTHORS: AUTHORS.rst
.. _CHANGES: CHANGES.rst
.. _README: README.rst


Adding migrations
-----------------

When you add new models or make changes to models, you'll need to make migrations before the tests will run.

To make migrations you can run::

    python runtests.py makemigrations


Testing
-------

Please add tests for your code and ensure existing tests don't break.  To run
the tests against your code::

    python runtests.py

Please use tox to test the code against supported Python and Django versions.
First install tox::

    pip install coverage tox

To run tox and generate a coverage report (in ``htmlcov`` directory)::

    make test
