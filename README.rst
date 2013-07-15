================
django-relatives
================

.. image:: https://travis-ci.org/treyhunner/django-relatives.png?branch=master
   :target: https://travis-ci.org/treyhunner/django-relatives
   :alt: Test Status

.. image:: https://coveralls.io/repos/treyhunner/django-relatives/badge.png?branch=master
   :target: https://coveralls.io/r/treyhunner/django-relatives
   :alt: Coverage Status

.. image:: https://pypip.in/v/django-relatives/badge.png
   :target: https://crate.io/packages/django-relatives
   :alt: Latest Version

.. image:: https://pypip.in/d/django-relatives/badge.png
   :target: https://crate.io/packages/django-relatives
   :alt: Download Count

Utilities for linking to related objects in Django admin

This app requires Django 1.5 or greater and Python 2.6 or greater.


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

Use hyperlinks for read-only foreign keys on change forms
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: https://raw.github.com/treyhunner/django-relatives/master/docs/images/contents_or_fk_link_example.png
   :target: https://django-relatives.readthedocs.org/en/latest/usage.html#linking-to-foreign-keys

Add edit links to admin inlines
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: https://raw.github.com/treyhunner/django-relatives/master/docs/images/object_edit_link_example.png
   :target: https://django-relatives.readthedocs.org/en/latest/usage.html#customizing-inline-edit-links

Link to reverse relations from from change forms
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: https://raw.github.com/treyhunner/django-relatives/master/docs/images/related_objects_example.png
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
