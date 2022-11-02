from click import password_option
from rest_framework import serializers
from .models import Account


class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = ["id", "username", "first_name", "last_name", "phone_number",
                  "is_medic", "is_active", "password"]
        extra_kwargs = {'password': {'write_only': True},
                        'first_name': {'required': True},
                        'last_name': {'required': True},
                        'phone_number': {'required': True}}

    def create(self, validated_data):
        return Account.objects.create_user(**validated_data)
