================
django-relatives
================

.. image:: https://img.shields.io/pypi/v/django-relatives.svg
   :target: https://pypi.org/project/django-relatives/
   :alt: PyPI

.. image:: https://img.shields.io/pypi/pyversions/django-relatives
   :target: https://pypi.org/project/django-relatives
   :alt: Python Version

.. image:: https://img.shields.io/pypi/djversions/django-relatives
   :target: https://pypi.org/project/django-relatives
   :alt: Django Version

.. image:: https://img.shields.io/readthedocs/django-relatives/latest.svg?label=Read%20the%20Docs
   :target: https://django-relatives.readthedocs.io/
   :alt: Read the documentation at https://django-relatives.readthedocs.io/

.. image:: https://github.com/treyhunner/django-relatives/workflows/Tests/badge.svg
   :target: https://github.com/treyhunner/django-relatives/actions?workflow=Tests
   :alt: Tests

.. image:: https://codecov.io/gh/treyhunner/django-relatives/branch/main/graph/badge.svg
   :target: https://codecov.io/gh/treyhunner/django-relatives
   :alt: Codecov

Utilities for linking to related objects in Django admin

This app requires Django 3.2 or greater and Python 3.8 or greater.


Getting Help
------------

Documentation for django-relatives is available at
https://django-relatives.readthedocs.org/

This app is available on `PyPI`_.

Submit issues on Github: https://github.com/treyhunner/django-relatives/issues

Pull requests are welcome.  Read the CONTRIBUTING file for tips on submitting
a pull request.

.. _PyPI: https://pypi.python.org/pypi/django-relatives/


Screenshots
-----------

.. image:: https://raw.github.com/treyhunner/django-relatives/master/docs/images/contents_or_fk_link_example.png
   :alt: Use hyperlinks for read-only foreign keys on change forms
   :target: https://django-relatives.readthedocs.org/en/latest/usage.html#linking-to-foreign-keys

.. image:: https://raw.github.com/treyhunner/django-relatives/master/docs/images/object_edit_link_example.png
   :alt: Add edit links to admin inlines
   :target: https://django-relatives.readthedocs.org/en/latest/usage.html#customizing-inline-edit-links

.. image:: https://raw.github.com/treyhunner/django-relatives/master/docs/images/related_objects_example.png
   :alt: Link to reverse relations from from change forms
   :target: https://django-relatives.readthedocs.org/en/latest/usage.html#linking-to-reverse-relations

Related Projects
----------------

Thanks to the community for inspiration:

- `linked readonly foreign key code snippet`_
- `django-inlaws`_
- various `StackOverflow answers`_ about related object links in admin

.. _django-inlaws: https://github.com/callowayproject/django-inlaws
.. _stackoverflow answers: http://stackoverflow.com/a/5331032/98187
.. _linked readonly foreign key code snippet: http://djangosnippets.org/snippets/2657/
