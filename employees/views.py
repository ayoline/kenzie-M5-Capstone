from rest_framework import generics
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from .permissions import IsOwnerOrIsAdmin


class EmployeeDetailListView(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeView(generics.CreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]

    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeDetailView(generics.RetrieveAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsOwnerOrIsAdmin]

    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_url_kwarg = "employee_id"


class EmployeeDetailView(generics.UpdateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]

    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_url_kwarg = "employee_id"


class EmployeeDetailView(generics.DestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]

    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_url_kwarg = "employee_id"
