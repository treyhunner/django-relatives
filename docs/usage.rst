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


Linking to objects which reference us
-------------------------------------

The ``related_objects`` template tag makes it easy to link to change lists filtered for reverse relations (objects that have a foreign key to a given object).

Django Relatives also provides a custom ``change_form.html`` template that may be used to add a "Relations" sidebar to change forms.  This sidebar provides links to change list queries for all objects that contain a foreign key to the current object.

To use the custom fieldset template you must add ``relatives`` to
``INSTALLED_APPS`` in your settings file:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'relatives',
    )

Now you can customize the change form template for your desired models/apps.  Either:

1. Set the ``change_form_template`` in your custom model admin
2. Override your model's ``change_form.html`` template

Customize ModelAdmin
~~~~~~~~~~~~~~~~~~~~

The easiest way to link to reverse relations is to override the ``change_form_template`` in your ``ModelAdmin`` subclass:

.. code-block:: python

    from django.contrib import admin

    from models import Company, Employee


    class CompanyAdmin(admin.ModelAdmin):
        change_form_template = 'relatives/change_form.html'

    admin.site.register(Company, CompanyAdmin)


    admin.site.register(Employee)

Custom template
~~~~~~~~~~~~~~~

If you don't have access to change the ``ModelAdmin`` for your model or you are already customizing your model's admin change form, you will need to use a custom admin template.

Create a ``admin/YOURAPP/YOURMODEL/change_form.html`` template file that extends from ``relatives/change_form.html``::

    {% include "relatives/change_form.html" %}

Also make sure this template file is in a custom template directory or an app
listed before your admin app in ``INSTALLED_APPS``.

Result
~~~~~~

Both of the above methods will result in the following:

.. figure:: images/related_objects_example.png
