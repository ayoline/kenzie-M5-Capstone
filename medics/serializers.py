from .models import Medic
from addresses.serializers import AddressSerializer
from categories.serializers import CategorySerializer
from specialties.serializers import SpecialtySerializer
from accounts.models import Account
from addresses.models import Address
from categories.models import Category
from specialties.models import Specialty
from rest_framework import serializers
from django.shortcuts import get_object_or_404
from django.http import Http404
from rest_framework.exceptions import NotFound


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = [
            "id",
            "first_name",
            "last_name",
            "phone_number",
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


class MedicSerializer(serializers.ModelSerializer):
    address = AddressSerializer()
    category = CategorySerializer(read_only=True)
    specialty = SpecialtySerializer(read_only=True)
    account = AccountSerializer()

    category_id = serializers.IntegerField(write_only=True)

    specialty_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Medic
        fields = [
            "id",
            "crm",
            "address",
            "category",
            "specialty",
            "account",
            "category_id",
            "specialty_id",
        ]

    def create(self, validated_data):
        body = {**validated_data}

        account_data = body.pop("account")

        crm = body.pop("crm")

        address_data = body.pop("address")

        category_data = body.pop("category_id")

        specialty_data = body.pop("specialty_id")

        try:
            category = get_object_or_404(Category, pk=category_data)
        except Http404:
            raise NotFound("Category not found!")

        try:
            specialty = get_object_or_404(Specialty, pk=specialty_data)
        except Http404:
            raise NotFound("Specialty not found!")

        account = Account.objects.create_user(**account_data, is_medic=True)

        address = Address.objects.create(**address_data)

        medic_data = {"crm": crm}

        medic = Medic.objects.create(
            **medic_data,
            account=account,
            category=category,
            specialty=specialty,
            address=address
        )

        return medic

    def update(self, instance, validated_data):
        body = {**validated_data}
        account_data = body.pop("account", None)

        crm = body.pop("crm", None)

        address_data = body.pop("address", None)

        category_data = body.pop("category_id", None)

        specialty_data = body.pop("specialty_id", None)

        if account_data is not None:
            for key, value in account_data.items():
                setattr(instance.account, key, value)

        instance.account.save()

        if address_data is not None:
            for key, value in address_data.items():
                setattr(instance.address, key, value)

            instance.address.save()

        if category_data is not None:
            category = get_object_or_404(Category, pk=category_data)
            instance.category = category

        if specialty_data is not None:
            specialty = get_object_or_404(Specialty, pk=specialty_data)
            instance.specialty = specialty

        if crm is not None:
            instance.crm = crm

        instance.save()

        return instance


class MedicListSerializer(serializers.ModelSerializer):
    category_id = serializers.IntegerField(read_only=True)
    specialty_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Medic
        fields = [
            "id",
            "crm",
            "category_id",
            "specialty_id",
        ]

        read_only_fields = [
            "id",
            "crm",
            "category_id",
            "specialty_id",
        ]
