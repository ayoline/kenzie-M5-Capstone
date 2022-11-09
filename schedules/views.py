from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView, RetrieveAPIView
from rest_framework.generics import ListCreateAPIView, DestroyAPIView
from .models import Schedule
from .serializers import ScheduleSerializer, SchedulePatchSerializer
from rest_framework.authentication import TokenAuthentication
from .permissions import (
    IsOwnerOrIsAuthOnCreate,
    IsOwnerOrIsAuthOnPatch,
    IsMedicOwnerOrIsAdmin
)
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from utils.mixins import SerializerByMethodMixin


class SchedulesPatientView(ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsOwnerOrIsAuthOnCreate]

    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer

    def get_queryset(self):
        patient_id = self.kwargs["patient_id"]
        return self.queryset.filter(patient_id=patient_id).all()

    def perform_create(self, serializer):
        patient_id = self.kwargs["patient_id"]
        serializer.save(patient_id=patient_id)


class SchedulesDetailsPatientView(SerializerByMethodMixin, RetrieveUpdateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsOwnerOrIsAuthOnPatch]

    queryset = Schedule.objects.all()

    serializer_map = {
        "GET": ScheduleSerializer,
        "PATCH": SchedulePatchSerializer,
    }


class SchedulesMedicView(ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsOwnerOrIsAuthOnCreate]
    lookup_url_kwarg = "medic_id"

    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer

    def get_queryset(self):
        medic_id = self.kwargs["medic_id"]
        return self.queryset.filter(medic_id=medic_id)


class SchedulesPatientCancelView(DestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsOwnerOrIsAuthOnPatch]

    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer

    def perform_destroy(self, instance):
        setattr(instance, "is_active", False)
        instance.save()
