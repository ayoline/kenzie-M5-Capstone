from rest_framework import serializers
from .models import Medic
from addresses.serializers import AddressSerializer
from categories.serializers import CategorySerializer
from specialties.serializers import SpecialtySerializer
from accounts.serializers import AccountSerializer


class MedicSerializer(serializers.ModelSerializer):
    address = AddressSerializer()
    category = CategorySerializer()
    specialty = SpecialtySerializer()
    account = AccountSerializer()

    class Meta:
        model = Medic
        fields = ["id", "crm", "address", "category", "specialty", "account"]

    def create(self, validated_data):
        body = {**validated_data}
        first_name = body.pop("first_name")
        last_name = body.pop("last_name")
        phone_number = body.pop("phone_number")
        username = body.pop("username")
        password = body.pop("password")

        crm = body.pop("crm")

        address = body.pop("address") 

        category = body.pop("category")

        specilty = body.pop("specilty")

        

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()

        return instance
