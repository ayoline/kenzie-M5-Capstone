from django.urls import path
from .views import ListCreateCategoriesView

urlpatterns = [
    path("category/", ListCreateCategoriesView.as_view()),
]
