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
