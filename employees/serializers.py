from rest_framework import serializers
from .models import Employee
from addresses.serializers import AddressSerializer
from accounts.serializers import AccountSerializer


class EmployeeSerializer(serializers.ModelSerializer):
    address = AddressSerializer()
    account = AccountSerializer()

    class Meta:
        model = Employee
        fields = [
            "id",
            "account",
            "cpf",
            "address",
        ]
