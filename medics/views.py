from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from .models import Medic
from .serializers import MedicSerializer


class MedicView(ListCreateAPIView):
    queryset = Medic.objects.all()
    serializer_class = MedicSerializer


class MedicDetailsView(RetrieveUpdateDestroyAPIView):
    queryset = Medic.objects.all()
    serializer_class = MedicSerializer
    