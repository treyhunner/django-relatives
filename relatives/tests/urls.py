from django.contrib import admin
from django.urls import path

admin.autodiscover()

urlpatterns = [
    path("adm/", admin.site.urls),
]
