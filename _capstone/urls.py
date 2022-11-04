from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("specialties.urls")),
    path("api/", include("categories.urls")),
    path("api/", include("employees.urls")),
    path("api/", include("medics.urls")),
    path("api/", include("patients.urls")),
    path("api/", include("accounts.urls")),
    path("api/", include("schedules.urls")),
]
