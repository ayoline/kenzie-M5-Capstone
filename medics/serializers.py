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
        fields = [
            "id",
            "crm",
            "address",
            "category",
            "specialty",
            "account"
        ]
