from django.contrib import admin

from .. import RelativesAdmin, link_related
from . import models


class ShapeAdmin(admin.ModelAdmin):
    readonly_fields = ["name", "lower_name", "upper_name"]

    def upper_name(self, obj):
        return obj.name.upper()


admin.site.register(models.Shape, ShapeAdmin)


class ShipAdmin(admin.ModelAdmin):
    change_form_template = "relatives/change_form.html"
    readonly_fields = ["name"]


admin.site.register(models.Ship, ShipAdmin)


class SailorAdmin(RelativesAdmin):
    readonly_fields = ["ship"]
    list_display = ["name", "ship", "ship_name"]


admin.site.register(models.Sailor, SailorAdmin)


class PetAdmin(admin.ModelAdmin):
    readonly_fields = ["owner"]


admin.site.register(models.Pet, PetAdmin)


class ImageAdmin(admin.ModelAdmin):
    readonly_fields = ["content_object"]


admin.site.register(models.Image, ImageAdmin)


class MealAdmin(admin.ModelAdmin):
    list_display = ["name", "prep", "rev"]

    @link_related("prepared")
    def prep(self, obj):
        return obj.prepared.name

    prep.short_description = "cook"

    @link_related("reviewed")
    def rev(self, obj):
        if obj.reviewed:
            return obj.reviewed.name[:4] + "..."

    rev.empty_value_display = "No one"


admin.site.register(models.Movie)
admin.site.register(models.Actor)
admin.site.register(models.Book)
admin.site.register(models.Journal)
admin.site.register(models.Eater)
admin.site.register(models.Meal, MealAdmin)
