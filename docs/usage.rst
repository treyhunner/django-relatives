Usage
=====

Installation
------------

Install from `PyPI`_:

.. code-block:: bash

    $ pip install django-relatives

.. _PyPI: https://pypi.python.org/pypi/django-relatives/


Edit links in inlines
---------------------

.. code-block:: python

    from django.contrib import admin
    from relatives.utils import object_link

    from models import Company, Employee


    class EmployeeInline(admin.TabularInline):
        model = Employee
        fields = [object_link, 'first_name', 'last_name']
        readonly_fields = fields
        extra = 0
        max_num = 0
        can_delete = False


    class CompanyAdmin(admin.ModelAdmin):
        inlines = [EmployeeInline]

    admin.site.register(Company, CompanyAdmin)


    admin.site.register(Employee)

Result:

.. figure:: images/object_link_example.png


Customizing edit link text
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    from django.contrib import admin
    from relatives.utils import object_edit_link

    from models import Company, Employee


    class EmployeeInline(admin.TabularInline):
        model = Employee
        edit_link = object_edit_link("Edit")
        fields = [edit_link, 'employee_id', 'first_name', 'last_name']
        readonly_fields = [edit_link]


    class CompanyAdmin(admin.ModelAdmin):
        inlines = [EmployeeInline]

    admin.site.register(Company, CompanyAdmin)


    admin.site.register(Employee)

Result:

.. figure:: images/object_edit_link_example.png


Linking to foreign keys
-----------------------

The ``contents_or_fk_link`` template filter can be used to link to foreign keys
for readonly admin form fields.

Django Relatives also provides a replacement for the
``admin/includes/fieldset.html`` template which can be used to automatically
link to all readonly foreign key fields in change forms.

To use the custom fieldset template you must add ``relatives`` to
``INSTALLED_APPS`` in your settings file:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'relatives',
    )

Next create a ``admin/includes/fieldset.html`` template file::

    {% include "relatives/includes/fieldset.html" %}

Also make sure this template file is in a custom template directory or an app
listed before your admin app in ``INSTALLED_APPS``.

Result:

.. figure:: images/contents_or_fk_link_example.png
