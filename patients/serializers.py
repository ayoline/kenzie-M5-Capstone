from rest_framework import serializers
from .models import Patient
from addresses.serializers import AddressSerializer
from categories.serializers import CategorySerializer
from charts.serializers import ChartSerializer


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
        body = { **validated_data }
        dataGroup = body.pop('group')
        dataTraits = body.pop('traits')

        obj2, created = Group.objects.get_or_create(
        name=dataGroup['name'],
        scientific_name=dataGroup['scientific_name'],
        )

        traits = []

        for item in dataTraits:
            obj, created = Trait.objects.get_or_create(
            name=item['name'],
            )
            traits.append(obj)

            animal = Animal.objects.create(**body, group=obj2)

            animal.traits.set(traits)

        return animal

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            if key == 'group' or  key == 'traits' or  key == 'sex':
                message = {f"{key}": f"You can not update {key} property."}
                raise NotUpdateFieldError(message)
            setattr(instance, key, value)
        
        instance.save()

        return instance
