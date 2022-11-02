from rest_framework.generics import ListCreateAPIView
from .models import Medic
from .serializers import MedicSerializer


class MedicView(ListCreateAPIView):
    queryset = Medic.objects.all()
    serializer_class = MedicSerializer
