from rest_framework import generics
from .models import Medic
from rest_framework.exceptions import PermissionDenied
from schedules.models import Schedule
from .serializers import MedicSerializer, MedicListSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAdminUser
from .permissions import IsOwnerOrIsAdmin, GetorIsAdmin
from utils.mixins import SerializerByMethodMixin


class MedicView(SerializerByMethodMixin, generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [GetorIsAdmin]

    queryset = Medic.objects.all()
    serializer_map = {
        "GET": MedicListSerializer,
        "POST": MedicSerializer,
    }


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
