from __future__ import unicode_literals
from django.utils.encoding import smart_text
from .compat import format_html
from django.contrib.contenttypes.models import ContentType
from django.urls import reverse, NoReverseMatch
from django.core.cache import cache
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey


def get_admin_url(obj):
    """Return admin URL for given object (raise NoReverseMatch on error)"""
    options = obj._meta.app_label, obj._meta.model_name
    return reverse('admin:%s_%s_change' % options, args=[obj.pk])


def object_edit_link(edit_text=None, blank_text=None):

    """
    Return function that takes an object and returns admin link to object

    Arguments:

    - ``edit_text`` is displayed in link text
    - ``blank_text`` is displayed in unlinked text (when no admin link)

    ``edit_text`` defaults to the object's unicode representation and
    ``blank_text`` defaults to the object's unicode representation if
    ``edit_text`` is None and an empty string otherwise
    """

    def object_link(obj):
        "Return admin link to given object or blank text if no link"
        link_text = smart_text(obj) if edit_text is None else edit_text
        try:
            if obj.pk:
                return format_html('<a href="{0}">{1}</a>', get_admin_url(obj),
                                   link_text)
        except NoReverseMatch:
            pass
        if blank_text is None:
            if edit_text is None:
                return link_text
            else:
                return ""
        else:
            return blank_text
    object_link.__name__ = str("")
    object_link.allow_tags = True
    return object_link


object_link = object_edit_link()
object_link.allow_tags = True
object_link.__doc__ += "\n\nEquivalent to object_edit_link()(obj)"


class RelatedObject(object):
    '''Generates fake django RelatedObject
    '''

    def __init__(self, field, ct_pk):
        self.field = field
        self.field.name = self.generate_field_name(field, ct_pk)
        self.model = self.field.model
        self.name = self.generate_name(field)

    @staticmethod
    def generate_name(field):
        return ':'.join([field.model._meta.app_label,
                        field.model._meta.model_name])

    @staticmethod
    def generate_field_name(field, ct_pk):
        return ''.join(
            map(str, [field.ct_field, '=', ct_pk, '&', field.fk_field]))


class GenericObjects(object):
    '''
    Search GenericForeignKey over all models
    and returns related objects if has relations with given object.
    '''

    def __init__(self, _object):
        self.obj = _object
        self.ct_pk = ContentType.objects.get_for_model(_object).pk
        self.cache_key = getattr(settings, 'RELATIVES_CACHE_KEY',
                                 'relatives_cache')
        self.cache_time = getattr(settings, 'RELATIVES_CACHE_TIME',
                                  60 * 60 * 24)
        self.generic_objects = []

    def get_generic_objects(self):
        try:
            self._generic_fields_cache
        except AttributeError:
            self._fill_generic_fields_cache()
        for generic_field in self._generic_fields_cache:
            params = {generic_field.ct_field: self.ct_pk,
                      generic_field.fk_field: self.obj.pk}
            if generic_field.model.objects.filter(**params).exists():
                generic_object = RelatedObject(generic_field, self.ct_pk)
                self.generic_objects.append(generic_object)
        return self.generic_objects

    def _fill_generic_fields_cache(self):
        self._generic_fields_cache = cache.get(self.cache_key)
        if self._generic_fields_cache is not None:
            return
        self._generic_fields_cache = []
        for content_type in ContentType.objects.all():
            model_class = content_type.model_class()
            if not model_class:
                continue  # Model for content type doesn't exist anymore
            self._generic_fields_cache += [
                field
                for field in model_class._meta.private_fields
                if isinstance(field, GenericForeignKey)
            ]
        cache.set(self.cache_key, self._generic_fields_cache, self.cache_time)
