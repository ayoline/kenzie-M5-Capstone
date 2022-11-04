from django.test import TestCase
from schedules.models import Schedule
from medics.models import Medic
from patients.models import Patient
from specialties.models import Specialty
from charts.models import Chart
from categories.models import Category
from addresses.models import Address
from accounts.models import Account


class SchedulesModelTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.schedule_data = {
            "description": "algo para testar",
            "start_at": "2022-11-04",
            "completed": False,
            "step": 1,
            "is_active": True,
            "medic_id": 1,
            "patient_id": 1,
            "specialty_id": 1,
        }
        cls.schedule = Schedule.objects.create(**cls.schedule_data)
        # ----------------------------------------------------------------------#
        cls.medic_data = {
            "crm": "12554663",
            "account_id": 1,
            "address_id": 1,
            "specialty_id": 1,
            "category_id": 1,
        }
        cls.medic = Medic.objects.create(**cls.medic_data)
        # ----------------------------------------------------------------------#

        cls.patient_data = {
            "first_name": "gabriela",
            "last_name": "laryssa",
            "cpf": "123285161",
            "address_id": 1,
            "category_id": 1,
            "chart_id": 1,
        }
        cls.patient = Patient.objects.create(**cls.patient_data)
        cls.chart_data = {
            "is_pregnant": True,
            "is_diabetic": True,
            "is_smoker": True,
            "is_allergic": True,
            "heart_disease": True,
            "dificulty_healing": True,
            "use_medication": True,
            "other_information": "inf teste",
        }
        cls.chart = Chart.objects.create(**cls.chart_data)
        cls.category_data = {
            "color": "azul",
            "description": "dsGEVE",
        }
        cls.category = Category.objects.create(**cls.category_data)
        cls.address_data = {
            "street": "testando",
            "number": 125,
            "cep": "1254385",
            "district": "aaaaaaa",
            "city": "mossoro",
            "state": "rn",
        }
        cls.address = Address.objects.create(**cls.address_data)
        cls.account_data = {
            "first_name": "aaaaaaaaaaaaaa",
            "last_name": "aaaaaaaaaaa",
            "username": "gabrieularyssa",
            "phone_number": "25465651215",
            "is_medic": False,
        }
        cls.account = Account.objects.create(**cls.account_data)
        #
        # ----------------------------------------------------------------------#
        cls.specialty_data = {
            "name": "otorrino",
        }
        cls.specialty = Specialty.objects.create(**cls.specialty_data)

    def test_schedule_attribute(self):
        """
        verifica se o banco de dados esta persistindo o atributo corretamente
        """
        # expected_max_length = 50
        # result_max_length = Medic._meta.get_field("crm").max_length
        expected_bool = 1
        return_boll = False

        self.assertEqual(self.schedule.description, self.schedule_data["description"])
        self.assertEqual(self.schedule.start_at, self.schedule_data["start_at"])
        self.assertEqual(self.schedule.completed, self.schedule_data["completed"])
        self.assertEqual(self.schedule.step, self.schedule_data["step"])
        self.assertEqual(self.schedule.is_active, self.schedule_data["is_active"])
