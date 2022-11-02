from rest_framework import serializers
from .models import Patient
from addresses.serializers import AddressSerializer
from categories.serializers import CategorySerializer
from charts.serializers import ChartSerializer


class PatientSerializer(serializers.ModelSerializer):
    address = AddressSerializer()
    category = CategorySerializer()
    chart = ChartSerializer()

    class Meta:
        model = Patient
        fields = [
            "id",
            "first_name",
            "last_name",
            "cpf",
            "address",
            "category",
            "chart",
        ]
