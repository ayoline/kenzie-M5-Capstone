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

    def create(self, validated_data):
        body = {**validated_data}
        first_name = body.pop("first_name")
        last_name = body.pop("last_name")
        phone_number = body.pop("phone_number")
        username = body.pop("username")
        password = body.pop("password")

        cpf = body.pop("cpf")

        address_data = body.pop("address") 

        chart_data = body.pop("chart") 

        category_data = body.pop("category")

        category = get_object_or_404(Category, color=category_data)

        account = Account.objects.create_user({
            "first_name": first_name,
            "last_name": last_name,
            "phone_number": phone_number,
            "username": username,
            "password": password,
            "is_medic": False
        })

        address = Address.objects.create({**address_data})

        chart = Chart.objects.create({**chart_data})

        patient = Patient.objects.create(
            {"cpf": cpf}, 
            address=address,
            category=category,
            chart=chart,
            account=account
        )

        return patient

    def update(self, instance, validated_data):
        ...
