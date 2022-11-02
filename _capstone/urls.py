from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("categories.urls")),
    path("api/", include("medics.urls")),
    path("api/", include("patients.urls")),
]
