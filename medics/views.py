from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from .models import Medic
from rest_framework.exceptions import PermissionDenied
from schedules.models import Schedule
from .serializers import MedicSerializer


class MedicView(ListCreateAPIView):
    queryset = Medic.objects.all()
    serializer_class = MedicSerializer


class MedicDetailsView(RetrieveUpdateDestroyAPIView):
    queryset = Medic.objects.all()
    serializer_class = MedicSerializer

    def perform_destroy(self, instance):
        schedule = Schedule.objects.all()

        if len(schedule.filter(medic_id=instance.id, completed=False)):
            raise PermissionDenied("Permission Denied: this medic has active schedules")

        instance.delete()
