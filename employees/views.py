from rest_framework import generics
from .models import Employee
from .serializers import EmployeeSerializer, EmployeeListSerializer
from rest_framework.authentication import TokenAuthentication
from .permissions import IsOwnerOrIsAdmin, IsAuthOrIsAdmin
from utils.mixins import SerializerByMethodMixin


class EmployeeView(SerializerByMethodMixin, generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthOrIsAdmin]

    queryset = Employee.objects.all()
    serializer_map = {
        "GET": EmployeeListSerializer,
        "POST": EmployeeSerializer,
    }


class EmployeeDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsOwnerOrIsAdmin]

    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_url_kwarg = "employee_id"
