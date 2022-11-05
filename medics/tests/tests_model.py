from django.test import TestCase
from accounts.models import Account
from medics.models import Medic
from specialties.models import Specialty
from categories.models import Category
from addresses.models import Address
from accounts.models import Account
from django.db import IntegrityError


class MedicsModelTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
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
            "is_medic": True,
        }
        cls.account = Account.objects.create_user(**cls.account_data)

        cls.medic_data = {
            "crm": "12545541541",
        }
        cls.medic = Medic.objects.create(**cls.medic_data, account=cls.account,
                                         address=cls.address, specialty=cls.specialty, category=cls.category)

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


class MedicRelationshipsTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.address_data = {
            "street": "rua das magueiras",
            "number": 100,
            "cep": "12345656",
            "state": "SP",
            "district": "bairro lalala",
            "city": "São Paulo",
        }

        cls.account_data = {
            "first_name": "fulano",
            "last_name": "de tal",
            "phone_number": "12345565565",
            "username": "hilarianey",
            "password": "sdada11231",
            "is_medic": True,
        }

        cls.medic_data = {
            "crm": "12312312315",
        }

        cls.category_data = {
            "color": "blue",
            "description": "Any description"
        }

        cls.chart_data = {
            "is_pregnant": False,
            "is_diabetic": False,
            "is_smoker": False,
            "is_allergic": False,
            "heart_disease": False,
            "dificulty_healing": False,
            "use_medication": False,
            "other_information": "test",
        }

        cls.specialty_data = {
            "name": "Clínico geral",
        }

        cls.account = Account.objects.create_user(**cls.account_data)
        cls.address = Address.objects.create(**cls.address_data)
        cls.specialty = Specialty.objects.create(**cls.specialty_data)
        cls.category = Category.objects.create(**cls.category_data)
        cls.medic = Medic.objects.create(
            **cls.medic_data, account=cls.account, address=cls.address, specialty=cls.specialty, category=cls.category)

    def test_if_medic_can_have_an_address(self):
        # Verifica se um medic pode registrar um address relacionado

        self.assertIs(self.address.medics, self.medic)

        self.assertIs(self.address, self.medic.address)

    def test_if_medic_can_have_an_account(self):
        # Verifica se um funcionário pode ter somente uma account relacionada

        self.assertIs(self.account.medics, self.medic)

        self.assertIs(self.account, self.medic.account)

    def test_if_raise_error_when_medic_already_have_an_address(self):
        """ Verifica se um erro é levantado ao atribuir o mesmo address a
        outro medic """

        with self.assertRaises(IntegrityError):
            account_two_data = {
                "first_name": "fulano",
                "last_name": "de tal",
                "phone_number": "12345565565",
                "username": "hilary",
                "password": "sdada11231",
                "is_medic": True,
            }

            medic_two_data = {
                "crm": "12312312329",
            }

            account = Account.objects.create_user(**account_two_data)
            medic_two = Medic.objects.create(
                **medic_two_data, account=account, address=self.address, specialty=self.specialty, category=self.category)

    def test_if_raise_error_when_medic_already_have_an_account(self):
        """ Verifica se um erro é levantado ao atribuir a mesma account a
        outro medic """

        with self.assertRaises(IntegrityError):
            address_two_data = {
                "street": "rua das magueiras",
                "number": 100,
                "cep": "12345656",
                "state": "SP",
                "district": "bairro lalala",
                "city": "São Paulo",
            }

            medic_two_data = {
                "crm": "12312314329",
            }

            address = Address.objects.create(**address_two_data)
            medic_two = Medic.objects.create(
                **medic_two_data, account=self.account, address=address, specialty=self.specialty, category=self.category)
