from rest_framework import serializers
from .models import Employee
from accounts.models import Account
from addresses.models import Address
from accounts.serializers import AccountSerializer
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

    def create(self, validated_data):
        account_data = validated_data.pop("account")
        account = Account.objects.create_user(**account_data)
        address_data = validated_data.pop("address")
        address = Address.objects.create(**address_data)
        employee = Employee.objects.create(
            **validated_data, account=account, address=address)
        return employee

    def update(self, instance, validated_data):

        account_data = validated_data.pop("account", None)

        cpf = validated_data.pop("cpf", None)

        address_data = validated_data.pop("address", None)

        if account_data:
            for key, value in account_data.items():
                setattr(instance.account, key, value)

            instance.account.save()

        if address_data:
            for key, value in address_data.items():
                setattr(instance.address, key, value)

            instance.address.save()

        if cpf is not None:
            instance.cpf = cpf

        instance.save()

        return instance
