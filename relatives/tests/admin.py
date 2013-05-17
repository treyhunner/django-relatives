from django.contrib import admin

from . import models


class ShipAdmin(admin.ModelAdmin):
    readonly_fields = ['name']


admin.site.register(models.Ship, ShipAdmin)


class SailorAdmin(admin.ModelAdmin):
    readonly_fields = ['ship']


admin.site.register(models.Sailor, SailorAdmin)
