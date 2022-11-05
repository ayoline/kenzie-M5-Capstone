from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.generics import RetrieveAPIView
from .models import Patient
from .serializers import PatientSerializer
from charts.models import Chart
from charts.serializers import ChartSerializer, ChartPatientSerializer


class PatientView(ListCreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


class PatientDetailsView(RetrieveUpdateDestroyAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


class PatientChartView(RetrieveAPIView):
    queryset = Chart.objects.all()
    serializer_class = ChartPatientSerializer
    lookup_url_kwarg = 'patient_id'
