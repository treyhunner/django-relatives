from django.conf import settings
from django.urls import path

from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    path("adm/", admin.site.urls),
]
