from rest_framework import generics
from .models import Medic
from rest_framework.exceptions import PermissionDenied
from schedules.models import Schedule
from .serializers import MedicSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAdminUser
from .permissions import IsOwnerOrIsAdmin


class MedicListView(generics.ListAPIView):
    queryset = Medic.objects.all()
    serializer_class = MedicSerializer


class MedicCreateView(generics.CreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]

    queryset = Medic.objects.all()
    serializer_class = MedicSerializer


class MedicDetailsView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsOwnerOrIsAdmin]

    queryset = Medic.objects.all()
    serializer_class = MedicSerializer
    lookup_url_kwarg = "medic_id"

    def perform_destroy(self, instance):
        schedule = Schedule.objects.all()

        if len(schedule.filter(medic_id=instance.id, completed=False)):
            raise PermissionDenied("Permission Denied: this medic has active schedules")

        instance.delete()
