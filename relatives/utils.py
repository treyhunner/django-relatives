from django.urls import reverse, NoReverseMatch
from django.utils.encoding import smart_str
from django.utils.html import format_html


def get_admin_url(obj):
    """Return admin URL for given object (raise NoReverseMatch on error)"""
    options = obj._meta.app_label, obj._meta.model_name
    return reverse("admin:%s_%s_change" % options, args=[obj.pk])


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
        link_text = smart_str(obj) if edit_text is None else edit_text
        try:
            if obj.pk:
                return format_html(
                    '<a href="{0}">{1}</a>', get_admin_url(obj), link_text
                )
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
