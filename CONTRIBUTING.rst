Contributing
============

Prerequisites
-------------

You'll need `uv <https://docs.astral.sh/uv/>`_ and `just <https://just.systems/>`_ installed.


Setup
-----

Clone the repo and run:

.. code-block:: bash

    $ just setup

This will create a virtual environment and install all dependencies.


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


Formatting & Linting
---------------------

This project uses `ruff <https://docs.astral.sh/ruff/>`_ for linting and formatting.

To auto-format and fix lint issues:

.. code-block:: bash

    $ just format

To check without modifying:

.. code-block:: bash

    $ just lint


Adding Migrations
-----------------

When you add new models or make changes to models, you'll need to make migrations before the tests will run:

.. code-block:: bash

    $ just makemigrations


Testing
-------

To run tests on your current Python version:

.. code-block:: bash

    $ just test

To run the full tox test matrix across Python and Django versions:

.. code-block:: bash

    $ just test-matrix

To run tests with a coverage report (in ``htmlcov`` directory):

.. code-block:: bash

    $ just test-cov


Documentation
-------------

To build the Sphinx documentation:

.. code-block:: bash

    $ just docs


Releases
--------

To release to PyPI:

1. Update the version: ``just bump patch`` (or ``minor``/``major``)
2. Build: ``just build``
3. Publish: ``just publish``
