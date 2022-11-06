from django.urls import path
from .views import MedicListView, MedicCreateView, MedicDetailsView

urlpatterns = [
    path("medic/", MedicListView.as_view()),
    path("medic/", MedicCreateView.as_view()),
    path("medic/<medic_id>/", MedicDetailsView.as_view()),
]
