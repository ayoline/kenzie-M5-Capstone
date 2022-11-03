from rest_framework import serializers
from .models import Medic
from addresses.serializers import AddressSerializer
from categories.serializers import CategorySerializer
from specialties.serializers import SpecialtySerializer
from accounts.serializers import AccountSerializer
from accounts.models import Account
from addresses.models import Address
from categories.models import Category
from specialties.models import Specialty
from django.shortcuts import get_object_or_404


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

        address_data = body.pop("address") 

        category_data = body.pop("category")

        specilty_data = body.pop("specilty")

        category = get_object_or_404(Category, color=category_data)

        specilty = get_object_or_404(Specialty, name=specilty_data)

        account = Account.objects.create_user({
            "first_name": first_name,
            "last_name": last_name,
            "phone_number": phone_number,
            "username": username,
            "password": password,
            "is_medic": True
        })

        address = Address.objects.create({**address_data})

        medic = Medic.objects.create(
            {"crm": crm}, 
            address=address,
            category=category,
            specialty=specilty,
            account=account
        )

        return medic
        
    def update(self, instance, validated_data):
        body = {**validated_data}
        first_name = body.pop("first_name", None)
        last_name = body.pop("last_name", None)
        phone_number = body.pop("phone_number", None)
        username = body.pop("username", None)
        password = body.pop("password", None)

        crm = body.pop("crm", None)

        address_data = body.pop("address", None) 

        category_data = body.pop("category", None)

        specilty_data = body.pop("specilty", None)

        data_account = {}

        if first_name is not None:
            data_account = {**data_account, "first_name": first_name}

        if last_name is not None:
            data_account = {**data_account, "last_name": last_name}

        if phone_number is not None:
            data_account = {**data_account, "phone_number": phone_number}

        if username is not None:
            data_account = {**data_account, "username": username}

        if password is not None:
            data_account = {**data_account, "password": password}

        for key, value in data_account.items():
            setattr(instance.user, key, value)
            
        instance.user.save()

        for key, value in address_data.items():
            setattr(instance.address, key, value)
            
        instance.address.save()

        if category_data is not None:
            category = get_object_or_404(Category, color=category_data)
            instance.category = category

        if specilty_data is not None:
            specilty = get_object_or_404(Specialty, name=specilty_data)
            instance.specilty = specilty

        if crm is not None:
            instance.crm = crm

        instance.save()

        return instance
