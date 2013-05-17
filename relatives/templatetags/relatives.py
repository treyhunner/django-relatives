from django.template import Library
from django.utils.safestring import mark_safe
from django.contrib.admin.util import lookup_field

from ..utils import get_admin_url


register = Library()


@register.filter
def contents_or_fk_link(field):
    contents = field.contents()
    field_name = field.field['field']
    obj = field.form.instance
    model_field = lookup_field(field_name, obj, field.model_admin)[0]
    if getattr(model_field, 'rel'):
        return mark_safe('<a href="%s">%s</a>' %
                         (get_admin_url(getattr(obj, field_name)), contents))
    else:
        return contents
