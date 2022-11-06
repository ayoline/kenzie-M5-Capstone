from django.urls import path
from rest_framework.authtoken.views import ObtainAuthToken
from . import views

urlpatterns = [
    path("employee/", views.EmployeeListView.as_view()),
    path("employee/", views.EmployeeCreateView.as_view()),
    path("employee/<employee_id>/", views.EmployeeDetailView.as_view()),
    path("login/", ObtainAuthToken.as_view()),
]
