from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView
from rest_framework.generics import ListCreateAPIView, DestroyAPIView
from .models import Schedule
from .serializers import ScheduleSerializer, SchedulePatchSerializer
from rest_framework.authentication import TokenAuthentication
from .permissions import IsOwnerOrIsAuthOnCreate, IsOwnerOrIsAuthOnPatch
from rest_framework.permissions import IsAdminUser


class SchedulesPatientView(ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsOwnerOrIsAuthOnCreate]

    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer

    def get_queryset(self):
        patient_id = self.kwargs["patient_id"]
        return self.queryset.filter(patient_id=patient_id)

    def perform_create(self, serializer):
        patient_id = self.kwargs["patient_id"]
        serializer.save(patient_id=patient_id)


class SchedulesDetailsPatientView(RetrieveUpdateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsOwnerOrIsAuthOnPatch]

    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer

    serializer_map = {
        'GET': ScheduleSerializer,
        'PATCH': SchedulePatchSerializer,
    }


class SchedulesMedicView(ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsOwnerOrIsAuthOnCreate]

    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer

    def get_queryset(self):
        medic_id = self.kwargs["medic_id"]
        return self.queryset.filter(medic_id=medic_id)


class SchedulesPatientCancelView(DestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]

    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer

    def perform_destroy(self, instance):
        setattr(instance, 'is_active', False)
        instance.save()
