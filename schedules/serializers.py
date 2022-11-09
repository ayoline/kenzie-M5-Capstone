from rest_framework import serializers
from .models import Schedule
from medics.serializers import MedicSerializer
from patients.serializers import PatientSerializer
from specialties.serializers import SpecialtySerializer
from medics.models import Medic
from patients.models import Patient
from specialties.models import Specialty
from .exceptions import (
    ConsultaEtapa1Error,
    MedicoPacienteCategoriasDiferentesError,
    ConsultaEtapa2Error,
    MedicoErradoError,
)
from django.shortcuts import get_object_or_404


class ScheduleSerializer(serializers.ModelSerializer):
    medic = MedicSerializer(read_only=True)
    patient = PatientSerializer(read_only=True)
    specialty = SpecialtySerializer(read_only=True)

    medic_id = serializers.IntegerField(write_only=True)
    patient_id = serializers.IntegerField(write_only=True)
    specialty_id = serializers.IntegerField(write_only=True)

    def validate_step(self, value):
        if not isinstance(value, int):
            raise serializers.ValidationError("step tem que ser um núemro inteiro.")
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
            "medic_id",
            "patient_id",
            "specialty_id",
            "is_active",
        ]
        read_only_fields = ["id", "completed", "is_active"]

    def create(self, validated_data):
        body = {**validated_data}
        step = body.get("step")
        medic_id = body.get("medic_id")
        patient_id = body.get("patient_id")
        specialty_id = body.get("specialty_id")

        medic = get_object_or_404(Medic, pk=medic_id)
        patient = get_object_or_404(Patient, pk=patient_id)
        specialty = get_object_or_404(Specialty, pk=specialty_id)

        if step == 1:
            if medic.category.color != patient.category.color:
                raise MedicoPacienteCategoriasDiferentesError()
            if medic.specialty.name != "Clínico Geral":
                raise ConsultaEtapa1Error()

        if step == 2:
            if medic.specialty.name == "Clínico Geral":
                raise ConsultaEtapa2Error()
            if medic.specialty.id != specialty.id:
                raise MedicoErradoError()

        schedule = Schedule.objects.create(**body)

        return schedule


class SchedulePatchSerializer(serializers.ModelSerializer):
    medic = MedicSerializer(read_only=True)
    patient = PatientSerializer(read_only=True)
    specialty = SpecialtySerializer(read_only=True)

    medic_id = serializers.IntegerField(write_only=True)
    patient_id = serializers.IntegerField(write_only=True)
    specialty_id = serializers.IntegerField(write_only=True)

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
            "medic_id",
            "patient_id",
            "specialty_id",
            "is_active",
        ]
        read_only_fields = ["id", "step", "is_active"]

    def update(self, instance, validated_data):

        step = instance.step
        medic_id = validated_data.get("medic_id", None)
        patient_id = validated_data.get("patient_id", None)
        specialty_id = validated_data.get("specialty_id", None)

        medic = instance.medic
        patient = instance.patient
        specialty = instance.specialty

        if medic_id is not None:
            medic = get_object_or_404(Medic, pk=medic_id)

        if patient_id is not None:
            patient = get_object_or_404(Patient, pk=patient_id)

        if specialty_id is not None:
            specialty = get_object_or_404(Specialty, pk=specialty_id)

        if step == 1:
            if medic.category.color != patient.category.color:
                raise MedicoPacienteCategoriasDiferentesError()
            if medic.specialty.name != "Clínico Geral":
                raise ConsultaEtapa1Error()

        if step == 2:
            if medic.specialty.name == "Clínico Geral":
                raise ConsultaEtapa2Error()
            if medic.specialty.id != specialty.id:
                raise MedicoErradoError()

        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()

        return instance
