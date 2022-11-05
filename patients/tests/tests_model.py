from django.test import TestCase
from patients.models import Patient
from categories.models import Category
from addresses.models import Address
from charts.models import Chart


class PatientsModelTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.patient_data = {
            "first_name": "Adriana",
            "last_name": "Silva",
            "cpf": "13678958236",
            "address_id": 2,
            "category_id": 2,
            "chart_id": 2,
        }
        cls.patient = Patient.objects.create(**cls.patient_data)

        cls.address_data = {
            "street": "Rua ValVerde",
            "number": 30,
            "cep": "14726826",
            "state": "MG",
            "district": "Centro",
            "city": "Belo Horizonte",
        }
        cls.address = Address.objects.create(**cls.address_data)

        cls.category_data = {
            "color": "verde",
            "description": "atende pela tarde",
        }
        cls.category = Category.objects.create(**cls.category_data)

        cls.chart_data = {
            "is_pregnant": False,
            "is_diabetic": True,
            "is_smoker": True,
            "is_allergic": True,
            "heart_disease": False,
            "dificulty_healing": False,
            "use_medication": True,
            "other_information": "Se encontra bem nervoso",
        }
        cls.chart = Chart.objects.create(**cls.chart_data)

    def test_patient_fields(self):
        self.assertEqual(self.patient.first_name, self.patient_data["first_name"])
        self.assertEqual(self.patient.last_name, self.patient_data["last_name"])
        self.assertEqual(self.patient.cpf, self.patient_data["cpf"])


class PatientRelationshipTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.address_data = {
            "street": "Rua ValVerde",
            "number": 30,
            "cep": "14726826",
            "state": "MG",
            "district": "Centro",
            "city": "Belo Horizonte",
        }

        cls.category_data = {
            "color": "verde",
            "description": "atende pela tarde",
        }

        cls.chart_data = {
            "is_pregnant": False,
            "is_diabetic": True,
            "is_smoker": True,
            "is_allergic": True,
            "heart_disease": False,
            "dificulty_healing": False,
            "use_medication": True,
            "other_information": "Se encontra bem nervoso",
        }

        cls.patient_data = {
            "first_name": "Adriana",
            "last_name": "Silva",
            "cpf": "13678958236",
            "address_id": 1,
            "category_id": 1,
            "chart_id": 1,
        }

        cls.chart = Chart.objects.create(**cls.chart_data)
        cls.address = Address.objects.create(**cls.address_data)
        cls.category = Category.objects.create(**cls.category_data)
        cls.patient = Patient.objects.create(
            **cls.patient_data,
            chart=cls.chart,
            address=cls.address,
            category=cls.category,
        )

    def test_if_patient_can_have_an_address(self):
        """
        Verifica se um patient pode registrar um address relacionado
        """

        self.assertIs(self.address.patients, self.patient)

        self.assertIs(self.address, self.patient.address)

    def test_cpf_max_length(self):
        """
        Verifica a propriedade de tamanho máximo de `cpf`
        """
        expected_max_length = 14
        result_max_length = Patient._meta.get_field("cpf").max_length
        msg = f"Verifique se a propriedade `max_length` de name foi definida como {expected_max_length}"

        self.assertEqual(expected_max_length, result_max_length, msg)
