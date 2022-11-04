from rest_framework import generics
from .models import Employee
from .serializers import EmployeeSerializer
from accounts.models import Account
from accounts.serializers import AccountSerializer


class EmployeeView(generics.ListCreateAPIView):

    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    """ def perform_destroy(self, instance):
        instance.account.is_active = False """
