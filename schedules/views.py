from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.generics import ListCreateAPIView, DestroyAPIView
from rest_framework.generics import UpdateAPIView
from .models import Schedule
from .serializers import ScheduleSerializer, SchedulePatchSerializer


class SchedulesPatientView(ListCreateAPIView):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer

    def get_queryset(self):
        patient_id = self.kwargs["patient_id"]
        return self.queryset.filter(patient_id=patient_id)

    def perform_create(self, serializer):
        patient_id = self.kwargs["patient_id"]
        serializer.save(patient_id=patient_id)


class SchedulesRetrievePatientView(RetrieveAPIView):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer


class SchedulesUpdatePatientView(UpdateAPIView):
    queryset = Schedule.objects.all()
    serializer_class = SchedulePatchSerializer


class SchedulesMedicView(ListAPIView):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer

    def get_queryset(self):
        medict_id = self.kwargs["medict_id"]
        return self.queryset.filter(medict_id=medict_id)


class SchedulesPatientCancelView(DestroyAPIView):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer

    def perform_destroy(self, instance):
        setattr(instance, 'is_active', False)
        instance.save()

