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

Testing
-------

Please add tests for your code and ensure existing tests don't break.  To run
the tests against your code::

    python setup.py test

Please use tox to test the code against supported Python and Django versions.
First install tox::

    pip install tox

To run tox and generate a coverage report (in ``htmlcov`` directory)::

    make test
