from django.urls import path
from .views import PatientView

urlpatterns = [
    path("patient/", PatientView.as_view()),
]
