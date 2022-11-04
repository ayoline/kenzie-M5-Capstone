from rest_framework import serializers
from .models import Chart

from patients.models import Patient
from addresses.serializers import AddressSerializer
from categories.serializers import CategorySerializer


class ChartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chart
        fields = [
            "is_pregnant",
            "is_diabetic",
            "is_smoker",
            "is_allergic",
            "heart_disease",
            "dificulty_healing",
            "use_medication",
            "other_information",
        ]


class PatientSerializer(serializers.ModelSerializer):
    address = AddressSerializer()
    category = CategorySerializer()

    class Meta:
        model = Patient
        fields = [
            "id",
            "first_name",
            "last_name",
            "cpf",
            "address",
            "category"
        ]


class ChartPatientSerializer(serializers.ModelSerializer):
    patients = PatientSerializer()

    class Meta:
        model = Chart
        fields = [
            "patients",
            "is_pregnant",
            "is_diabetic",
            "is_smoker",
            "is_allergic",
            "heart_disease",
            "dificulty_healing",
            "use_medication",
            "other_information",
        ]