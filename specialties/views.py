from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Specialty
from .serializers import SpecialtySerializer


class SpecialtyView(ListCreateAPIView):
    serializer_class = SpecialtySerializer
    queryset = Specialty.objects.all()


class SpecialtyDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = SpecialtySerializer
    queryset = Specialty.objects.all()
    lookup_url_kwarg = "specialty_id"
