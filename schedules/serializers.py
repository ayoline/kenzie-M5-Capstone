from rest_framework import serializers
from .models import Schedule
from medics.serializers import MedicSerializer
from patients.serializers import PatientSerializer
from specialties.serializers import SpecialtySerializer
from medics.models import Medic
from patients.models import Patient


class ScheduleSerializer(serializers.ModelSerializer):
    medic = MedicSerializer()
    patient = PatientSerializer()
    specialty = SpecialtySerializer()

    def validate_step(self, value):
        if not isinstance(value, int):
            raise serializers.ValidationError(
                "step tem que ser um núemro inteiro."
            )
        if value < 1 or value > 2:
            raise serializers.ValidationError(
                "stepe tem que ser um número inteiro de 1 a 2"
            )
        return value

    class Meta:
        model = Schedule
        fields = [
            "id",
            "description",
            "start_at",
            "completed",
            "step",
            "medic",
            "patient",
            "specialty",
        ]
        read_only_fields = [
            "id",
            "completed",
            "quantity"
        ]

    def create(self, validated_data):
        body = {**validated_data}
        step = body.get('step')
        medic_id = body.get('medic_id')
        patient_id = body.get('patient_id')

        medic = Medic.objects.get(pk=medic_id)
        patient = Patient.objects.get(pk=patient_id)

        if medic.category.cor != patient.category.cor:
            ...

        if step == 1 & medic.specialty.name != 'Clínico Geral':
            ...

        if step == 2 & medic.specialty.name == 'Clínico Geral':
            ...

        schedule = Schedule.objects.create(body)

        return schedule


class SchedulePatchSerializer(serializers.ModelSerializer):
    medic = MedicSerializer()
    patient = PatientSerializer()
    specialty = SpecialtySerializer()

    class Meta:
        model = Schedule
        fields = [
            "id",
            "description",
            "start_at",
            "completed",
            "step",
            "medic",
            "patient",
            "specialty",
        ]
        read_only_fields = [
            "id",
            "completed",
            "quantity",
            "step",
        ]

    def update(self, instance, validated_data):

        step = instance.step
        medic_id = validated_data.get('medic_id', None)
        patient_id = validated_data.get('patient_id', None)

        medic = instance.medic
        patient = instance.patient

        if medic_id is not None:
            medic = Medic.objects.get(pk=medic_id)

        if patient_id is not None:
            patient = Patient.objects.get(pk=patient_id)

        if medic.category.cor != patient.category.cor:
            ...

        if step == 1 & medic.specialty.name != 'Clínico Geral':
            ...

        if step == 2 & medic.specialty.name == 'Clínico Geral':
            ...

        for key, value in validated_data.items():
            setattr(instance, key, value)
        
        instance.save()

        return instance 