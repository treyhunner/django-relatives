from __future__ import unicode_literals
from django.utils.encoding import smart_text
from django.core.urlresolvers import NoReverseMatch
from django.core.urlresolvers import reverse


def get_admin_url(obj):
    """Return admin URL for given object (raise NoReverseMatch on error)"""
    options = obj._meta.app_label, obj._meta.module_name
    return reverse('admin:%s_%s_change' % options, args=[obj.pk])


def object_link(obj):
    """Return admin link to given object or object representation if no link"""
    link_text = smart_text(obj)
    try:
        if obj.pk:
            return '<a href="%s">%s</a>' % (get_admin_url(obj), link_text)
    except NoReverseMatch:
        pass
    return link_text
object_link.__name__ = str("")
object_link.allow_tags = True
