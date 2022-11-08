from django.test import TestCase
from schedules.models import Schedule
from medics.models import Medic
from patients.models import Patient
from specialties.models import Specialty
from categories.models import Category
from addresses.models import Address
from accounts.models import Account
from charts.models import Chart


class SchedulesRelationshipTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.schedule_data = {
            "description": "testando relacionamento",
            "start_at": "2022-11-26T01:40:000-03:00",
            "completed": False,
            "step": 1,
            "is_active": True,
        }
        cls.medic_data = {
            "crm": "2165161561651616",
        }
        cls.patient_data = {
            "first_name": "gabriela",
            "last_name": "laryssa",
            "cpf": "11122255544",
        }
        cls.address_data = {
            "street": "rua das estrelinhas douradas",
            "number": 13,
            "cep": "123456789",
            "district": "fazendo testes",
            "city": "mossoro",
            "state": "RN",
        }
        cls.category_data = {
            "color": "azul",
            "description": "atendimento matinal",
        }
        cls.specialty_data = {
            "name": "otorrino",
        }
        cls.account_medic_data = {
            "first_name": "gabriela",
            "last_name": "laryssa",
            "username": "gabrieularyssa",
            "phone_number": "84998110000",
            "is_medic": "True",
        }
        cls.account_patient_data = {
            "first_name": "adri",
            "last_name": "ana",
            "username": "adriana",
            "phone_number": "84998110000",
            "is_medic": "False",
        }
        cls.chart_data = {
            "is_pregnant": True,
            "is_diabetic": False,
            "is_smoker": True,
            "is_allergic": False,
            "heart_disease": False,
            "dificulty_healing": True,
            "use_medication": True,
            "other_information": "preenchendo campo para teste",
        }
        # cls.account_patient = Account.objects.create_user(**cls.account_patient_data)
        cls.account_medic = Account.objects.create_user(**cls.account_medic_data)
        cls.specialty = Specialty.objects.create(**cls.specialty_data)
        cls.address = Address.objects.create(**cls.address_data)
        cls.category = Category.objects.create(**cls.category_data)
        cls.chart = Chart.objects.create(**cls.chart_data)
        cls.medic = Medic.objects.create(
            **cls.medic_data,
            address=cls.address,
            category=cls.category,
            specialty=cls.specialty,
            account=cls.account_medic,
        )
        cls.patient = Patient.objects.create(
            **cls.patient_data,
            address=cls.address,
            category=cls.category,
            chart=cls.chart,
        )
        cls.schedule = Schedule.objects.create(
            **cls.schedule_data,
            medic=cls.medic,
            patient=cls.patient,
            specialty=cls.specialty,
        )

    def test_relationship_schedule_and_medic(self):
        """
        Verifica o relacionamento entre schedule e medico
        """
        expected_medic_crm = "2165161561651616"
        result_medic_crm = self.schedule.medic.crm

        self.assertEqual(expected_medic_crm, result_medic_crm)

    def test_relationship_schedule_and_patient(self):
        """
        Verifica o relacionamento entre schedule e paciente analisando o cpf
        """
        expected_patient_cpf = "11122255544"
        result_patient_cpf = self.schedule.patient.cpf

        self.assertEqual(expected_patient_cpf, result_patient_cpf)
