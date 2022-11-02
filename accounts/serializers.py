from rest_framework import serializers
from .models import Account


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = [
            "id",
            "first_name",
            "last_name",
            "phone_number",
            "is_medic",
            "username",
            "password",
            "is_superuser",
            "is_active",
        ]
        extra_kwargs = {"password": {"write_only": True}}

        read_only_fields = [
            "is_superuser",
            "is_active",
        ]

    def create(self, validated_data):
        return Account.objects.create_user(**validated_data)
