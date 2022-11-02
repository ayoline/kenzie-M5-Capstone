from django.urls import path
from .views import MedicView

urlpatterns = [
    path("medic/", MedicView.as_view()),
]
