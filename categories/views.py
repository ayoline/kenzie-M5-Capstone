from rest_framework.generics import ListCreateAPIView
from .serializers import CategorySerializer
from .models import Category


class ListCreateCategoriesView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
