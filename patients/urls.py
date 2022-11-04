from django.urls import path
from .views import PatientView, PatientDetailsView, PatientChartView

urlpatterns = [
    path("patient/", PatientView.as_view()),
    path("patient/<pk>/", PatientDetailsView.as_view()),
    path("patient/<patient_id>/chart/", PatientChartView.as_view()),
]
