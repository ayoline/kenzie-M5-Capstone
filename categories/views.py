from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import CategorySerializer
from .models import Category
from .permissions import GetRouteOrIsAdmin
from rest_framework.authentication import TokenAuthentication


class CategoryView(ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [GetRouteOrIsAdmin]

    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [GetRouteOrIsAdmin]

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_url_kwarg = "category_id"
