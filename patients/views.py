from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.generics import RetrieveAPIView
from .models import Patient
from .serializers import PatientSerializer
from charts.models import Chart
from charts.serializers import ChartPatientSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAdminOrAuth


class PatientView(ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


class PatientDetailsView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminOrAuth]

    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    lookup_url_kwarg = "patient_id"


class PatientChartView(RetrieveAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Chart.objects.all()
    serializer_class = ChartPatientSerializer
    lookup_url_kwarg = "patient_id"
