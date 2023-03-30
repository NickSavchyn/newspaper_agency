
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("newspaper_agency.urls", namespace="newspaper_agency")),
]
