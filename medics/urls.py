from django.urls import path
from .views import MedicDetailsView, MedicView

urlpatterns = [
    path("medic/", MedicView.as_view()),
    path("medic/<medic_id>/", MedicDetailsView.as_view()),
]
