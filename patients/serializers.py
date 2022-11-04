from rest_framework import serializers
from .models import Patient
from addresses.serializers import AddressSerializer
from categories.serializers import CategorySerializer
from charts.serializers import ChartSerializer
from accounts.models import Account
from addresses.models import Address
from categories.models import Category
from charts.models import Chart
from django.shortcuts import get_object_or_404


class PatientSerializer(serializers.ModelSerializer):
    address = AddressSerializer()
    category = CategorySerializer(read_only=True)
    chart = ChartSerializer()

    category_id = serializers.IntegerField(write_only=True)

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
            "category_id",
        ]

    def create(self, validated_data):
        body = {**validated_data}
        first_name = body.pop("first_name")
        last_name = body.pop("last_name")

        cpf = body.pop("cpf")

        address_data = body.pop("address") 

        chart_data = body.pop("chart") 

        category_data = body.pop("category_id")

        category = get_object_or_404(Category, pk=category_data)

        address = Address.objects.create(**address_data)

        chart = Chart.objects.create(**chart_data)

        pacient_data = {
            "cpf": cpf,
            "first_name": first_name,
            "last_name": last_name
        }

        patient = Patient.objects.create(
            **pacient_data, 
            address=address,
            category=category,
            chart=chart,
        )

        return patient

    def update(self, instance, validated_data):
        body = {**validated_data}
        first_name = body.pop("first_name", None)
        last_name = body.pop("last_name", None)

        cpf = body.pop("cpf", None)

        address_data = body.pop("address", None) 

        chart_data = body.pop("chart", None) 

        category_data = body.pop("category_id", None)

        if address_data is not None:
            for key, value in address_data.items():
                setattr(instance.address, key, value)
            
            instance.address.save()

        if chart_data is not None:
            for key, value in chart_data.items():
                setattr(instance.chart, key, value)
            
            instance.chart.save()

        if category_data is not None:
            category = get_object_or_404(Category, pk=category_data)
            instance.category = category

        if first_name is not None:
            instance.first_name = first_name

        if last_name is not None:
            instance.last_name = last_name

        if cpf is not None:
            instance.cpf = cpf

        instance.save()

        return instance
