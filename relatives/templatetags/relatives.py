from django.template import Library
from django.core.urlresolvers import reverse, NoReverseMatch
from django.utils.encoding import smart_text
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


@register.assignment_tag
def related_objects(obj):
    object_list = []
    related_objects = (obj._meta.get_all_related_objects() +
                       obj._meta.get_all_related_many_to_many_objects())
    for related in related_objects:
        try:
            url = reverse('admin:{0}_{1}_changelist'.format(
                          *related.name.split(':')))
        except NoReverseMatch:
            continue
        object_list.append({
            'plural_name': related.model._meta.verbose_name_plural,
            'url': smart_text('%s?%s=%s' % (url, related.field.name, obj.pk)),
        })
    return object_list
