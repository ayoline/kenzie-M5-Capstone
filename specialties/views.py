from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Specialty
from medics.models import Medic
from schedules.models import Schedule
from django.contrib import messages
from .serializers import SpecialtySerializer
from django.core.exceptions import PermissionDenied
from rest_framework import status
import ipdb


class SpecialtyView(ListCreateAPIView):
    serializer_class = SpecialtySerializer
    queryset = Specialty.objects.all()


class SpecialtyDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = SpecialtySerializer
    queryset = Specialty.objects.all()
    lookup_url_kwarg = "specialty_id"

    def perform_destroy(self, instance):
        medics = Medic.objects.all()
        schedule = Schedule.objects.all()
        clinic_general = "Clínico Geral"

        if len(medics.filter(specialty__id=instance.id)):
            raise PermissionDenied

        if len(schedule.filter(specialty_id=instance.id, completed=False)):
            raise PermissionDenied

        if instance.name.__contains__(clinic_general):
            raise PermissionDenied

        instance.delete()
