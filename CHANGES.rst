Changes
=======

1.2.0 (2020-12-15)
------------------

- Fix ModelAdmin methods used in read-only fields

1.1.0 (2020-01-28)
------------------

- Fix generic foreign key links on change forms
- Add support for Django 2.2 and Django 3.0
- Drop support for Python 2

1.0.0 (2018-08-07)
------------------

- Generic relations templatetag support implemented
- Add support for Django 1.11 through 2.1


0.3.1 (2013-07-27)
------------------

- Reintroduce Django 1.4 support


0.3.0 (2013-07-16)
------------------

- Fix XSS vulnerability
- Allow relatives/includes/fieldset.html template to be extended further
- Improve documentation


0.2.0 (2013-06-26)
------------------

- Add related_objects template tag
- Fix contents_or_fk_link filter on add form for non-nullable foreign keys
- Rename edit_link utility function to object_link
- Add generic object_edit_link utility
- Add generic templates for easy related_objects and contents_or_fk_link use


0.1.0 (2013-05-17)
------------------
Initial release.
