from django.contrib.admin import ModelAdmin
from django.core.exceptions import FieldDoesNotExist

from .utils import object_link


def relation_link(related_field):
    def object_relation_link(original_obj):
        obj = getattr(original_obj, related_field)
        if obj is not None:
            return object_link(obj)

    object_relation_link.__name__ = related_field
    object_relation_link.allow_tags = True
    object_relation_link.admin_order_field = related_field
    return object_relation_link


def related_link_or_attribute(model, attr):
    try:
        relation = model._meta.get_field(attr).is_relation
    except FieldDoesNotExist:
        relation = False
    if relation:
        return relation_link(attr)
    else:
        return attr


class RelativesMixin:
    """ModelAdmin mixin that makes list display foreign keys linked."""

    def get_list_display(self, request):
        return [
            related_link_or_attribute(self.model, attr) for attr in self.list_display
        ]


class RelativesAdmin(RelativesMixin, ModelAdmin):
    """ModelAdmin that links to related fields."""
