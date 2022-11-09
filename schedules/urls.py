from django.urls import path
from .views import SchedulesMedicView, SchedulesPatientCancelView
from .views import SchedulesPatientView, SchedulesDetailsPatientView

urlpatterns = [
    path(
        "patient/<patient_id>/schedule/<pk>/",
        SchedulesDetailsPatientView.as_view()
    ),
    # path("patient/<patient_id>/schedule/", SchedulePatientListView.as_view()),
    path("patient/<patient_id>/schedule/", SchedulesPatientView.as_view()),
    path("medic/<medic_id>/schedule/", SchedulesMedicView.as_view()),
    path(
        "patient/<patient_id>/schedule/<pk>/cancel/",
        SchedulesPatientCancelView.as_view(),
    ),
]
