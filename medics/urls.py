from django.urls import path
from .views import MedicView, MedicDetailsView

urlpatterns = [
    path("medic/", MedicView.as_view()),
    path("medic/<pk>/", MedicDetailsView.as_view()),
]
