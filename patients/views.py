from rest_framework.generics import ListCreateAPIView
from .models import Patient
from .serializers import PatientSerializer


class PatientView(ListCreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
