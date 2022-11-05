from rest_framework import generics
from .models import Employee
from .serializers import EmployeeSerializer


class EmployeeView(generics.ListCreateAPIView):

    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
