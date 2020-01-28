from django.contrib import admin

from . import models


class ShipAdmin(admin.ModelAdmin):
    readonly_fields = ['name']


admin.site.register(models.Ship, ShipAdmin)


class SailorAdmin(admin.ModelAdmin):
    readonly_fields = ['ship']


admin.site.register(models.Sailor, SailorAdmin)


class PetAdmin(admin.ModelAdmin):
    readonly_fields = ['owner']


admin.site.register(models.Pet, PetAdmin)


class ImageAdmin(admin.ModelAdmin):
    readonly_fields = ['content_object']


admin.site.register(models.Image, ImageAdmin)


admin.site.register(models.Movie)
admin.site.register(models.Actor)
admin.site.register(models.Book)
admin.site.register(models.Journal)
