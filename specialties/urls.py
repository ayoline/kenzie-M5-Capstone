from django.urls import path
from .views import SpecialtyView, SpecialtyDetailView

urlpatterns = [
    path("specialty/", SpecialtyView.as_view()),
    path("specialty/<int:specialty_id>/", SpecialtyDetailView.as_view()),
]
