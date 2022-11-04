from django.test import TestCase
from accounts.models import Account
from medics.models import Medic
from specialties.models import Specialty
from categories.models import Category
from addresses.models import Address
from accounts.models import Account


class MedicsModelTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.medic_data = {
            "crm": "12545541541",
            "account_id": 1,
            "address_id": 1,
            "category_id": 1,
            "specialty_id": 1,
        }
        cls.medic = Medic.objects.create(
            **cls.medic_data,
        )
        cls.specialty_data = {
            "name": "otorrino",
        }
        cls.specialty = Specialty.objects.create(**cls.specialty_data)
        cls.category_data = {
            "color": "vermelho",
            "description": "atende pela manha",
        }
        cls.category = Category.objects.create(**cls.category_data)
        cls.address_data = {
            "street": "uma rua qualquer",
            "number": 22,
            "cep": "5986521",
            "state": "rn",
            "district": "mossoro",
        }
        cls.address = Address.objects.create(**cls.address_data)
        cls.account_data = {
            "first_name": "gabriela",
            "last_name": "laryssa",
            "username": "gabrieularyssa",
            "phone_number": "896620",
            "is_medic": False,
        }
        cls.account = Account.objects.create(**cls.account_data)

    def test_medic_max_length_crm(self):
        """
        Verifica o numero de caracteres do CRM
        """
        expected_max_length = 50
        result_max_length = Medic._meta.get_field("crm").max_length
        self.assertEqual(expected_max_length, result_max_length)

    def test_attribute_received(self):
        """
        Verifica se crm esta sendo persistido como crm
        """
        self.assertEqual(self.medic.crm, self.medic_data["crm"])
