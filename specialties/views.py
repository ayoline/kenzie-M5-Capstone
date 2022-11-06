from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Specialty
from medics.models import Medic
from schedules.models import Schedule
from .serializers import SpecialtySerializer
from rest_framework.exceptions import PermissionDenied
from .permissions import GetRouteOrIsAdmin
from rest_framework.authentication import TokenAuthentication


class SpecialtyView(ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [GetRouteOrIsAdmin]

    serializer_class = SpecialtySerializer
    queryset = Specialty.objects.all()


class SpecialtyDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [GetRouteOrIsAdmin]

    serializer_class = SpecialtySerializer
    queryset = Specialty.objects.all()
    lookup_url_kwarg = "specialty_id"

    def perform_destroy(self, instance):
        medics = Medic.objects.all()
        schedule = Schedule.objects.all()
        clinic_general = "Clínico Geral"

        if len(medics.filter(specialty__id=instance.id)):
            raise PermissionDenied(
                "Permission Denied: this specialty is in use by a medic!"
            )

        if len(schedule.filter(specialty_id=instance.id, completed=False)):
            raise PermissionDenied(
                "Permission Denied: this specialty is in use by an active schedule!"
            )

        if instance.name.__contains__(clinic_general):
            raise PermissionDenied(
                "Permission Denied: specialty 'Clínico Geral' cannot be deleted"
            )

        instance.delete()
