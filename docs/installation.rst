Usage
=====

Installation
------------

Install from `PyPI`_:

.. code-block:: bash

    $ pip install django-relatives

.. _PyPI: https://pypi.python.org/pypi/django-relatives/


Since relatives uses cache, you can set settings to change the defaults:

.. code-block:: python

    RELATIVES_CACHE_KEY = 'relatives_cache'
    RELATIVES_CACHE_TIME = 60*60*24
