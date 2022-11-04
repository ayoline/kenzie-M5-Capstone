from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from .serializers import CategorySerializer
from .models import Category


class CategoryView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetailView(RetrieveUpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_url_kwarg = "category_id"
