from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from accounts.models import Account
from medics.models import Medic
from patients.models import Patient
from addresses.models import Address
from categories.models import Category
from specialties.models import Specialty
from schedules.models import Schedule
from charts.models import Chart


class SchedulesViewTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user_admin_data = {
            "first_name": "admin",
            "last_name": "admin",
            "phone_number": "99999999999",
            "username": "admin",
            "password": "admin",
            "is_medic": False,
        }

        cls.address_data_1 = {
            "street": "rua das magueiras",
            "number": 12345,
            "cep": "12345678",
            "state": "SP",
            "district": "bairro lalala",
            "city": 'São Paulo'
        }

        cls.address_data_2 = {
            "street": "rua das magueiras",
            "number": 12345,
            "cep": "12345678",
            "state": "SP",
            "district": "bairro lalala",
            "city": 'São Paulo'
        }

        cls.category_data_1 = {"color": "red", "description": "lalalala"}

        cls.category_data_2 = {"color": "blue", "description": "lalalala2"}

        cls.specialty_data_1 = {"name": "Clínico Geral"}

        cls.specialty_data_2 = {"name": "Otorrinolaringologista"}

        cls.schedule_data_1 = {
            "description": "paciente precisa de atenção pq tem convulsões",
            "start_at": "2022-11-01 10:00:00",
            "step": 1
        }

        cls.schedule_data_2 = {
            "description": "paciente precisa de atenção pq tem convulsões",
            "start_at": "2022-11-01 10:00:00",
            "step": 2
        }

        cls.account_data_1 = {
            "first_name": "soares",
            "last_name": "soares",
            "phone_number": "88888888888",
            "username": "soares",
            "password": "soares",
        }

        cls.account_data_2 = {
            "first_name": "ferreira",
            "last_name": "ferreira",
            "phone_number": "77777777777",
            "username": "ferreira",
            "password": "ferreira",
        }

        cls.chart_data_1 = {
            "is_pregnant": False,
            "is_diabetic": False,
            "is_smoker": False,
            "is_allergic": False,
            "heart_disease": False,
            "dificulty_healing": False,
            "use_medication": False,
            "other_information": "teste"
        }

        cls.chart_data_2 = {
            "is_pregnant": False,
            "is_diabetic": False,
            "is_smoker": False,
            "is_allergic": False,
            "heart_disease": False,
            "dificulty_healing": False,
            "use_medication": False,
            "other_information": "teste"
        }

        cls.patient_data_1 = {
            "first_name": "anderson",
            "last_name": "alves1",
            "cpf": "1232133434",
        }

        cls.patient_data_2 = {
            "first_name": "ferreira",
            "last_name": "alves2",
            "cpf": "1232133435",
        }

        cls.medic_data_1 = {"crm": "12312312312"}

        cls.medic_data_2 = {"crm": "12312312313"}

    """ rota create """

    def test_create_schedule_using_user_admin(self):
        admin = Account.objects.create_superuser(**self.user_admin_data)
        token = Token.objects.create(user=admin)

        self.client.credentials(HTTP_AUTHORIZATION="Token " + token.key)

        category = Category.objects.create(**self.category_data_1)

        specialty = Specialty.objects.create(**self.specialty_data_1)

        account = Account.objects.create_user(**self.account_data_1, is_medic=True)

        address_medic = Address.objects.create(**self.address_data_1)

        address_patient = Address.objects.create(**self.address_data_2)

        chart = Chart.objects.create(**self.chart_data_1)

        patient = Patient.objects.create(
            **self.patient_data_1,
            chart=chart,
            category=category,
            address=address_patient,
        )

        medic = Medic.objects.create(
            **self.medic_data_1,
            account=account,
            category=category,
            specialty=specialty,
            address=address_medic,
        )

        response = self.client.post(
            f"/api/patient/{patient.id}/schedule/",
            {
                **self.schedule_data_1,
                "medic_id": medic.id,
                "patient_id": patient.id,
                "specialty_id": specialty.id,
            },
            format="json",
        )

        self.assertEqual(response.status_code, 201)

        schedule = Schedule.objects.first()

        self.assertEqual(schedule.medic.id, medic.id)

        self.assertEqual(schedule.patient.id, patient.id)

        self.assertEqual(schedule.specialty.id, specialty.id)

        self.assertEqual(schedule.description, self.schedule_data_1["description"])

        self.assertEqual(schedule.step, self.schedule_data_1["step"])

    def test_create_schedule_using_user_employee(self):
        admin = Account.objects.create_user(**self.user_admin_data)
        token = Token.objects.create(user=admin)

        self.client.credentials(HTTP_AUTHORIZATION="Token " + token.key)

        category = Category.objects.create(**self.category_data_1)

        specialty = Specialty.objects.create(**self.specialty_data_1)

        account = Account.objects.create_user(**self.account_data_1, is_medic=True)

        address_medic = Address.objects.create(**self.address_data_1)

        address_patient = Address.objects.create(**self.address_data_2)

        chart = Chart.objects.create(**self.chart_data_1)

        patient = Patient.objects.create(
            **self.patient_data_1,
            chart=chart,
            category=category,
            address=address_patient,
        )

        medic = Medic.objects.create(
            **self.medic_data_1,
            account=account,
            category=category,
            specialty=specialty,
            address=address_medic,
        )

        response = self.client.post(
            f"/api/patient/{patient.id}/schedule/",
            {
                **self.schedule_data_1,
                "medic_id": medic.id,
                "patient_id": patient.id,
                "specialty_id": specialty.id,
            },
            format="json",
        )

        self.assertEqual(response.status_code, 201)

        schedule = Schedule.objects.first()

        self.assertEqual(schedule.medic.id, medic.id)

        self.assertEqual(schedule.patient.id, patient.id)

        self.assertEqual(schedule.specialty.id, specialty.id)

        self.assertEqual(schedule.description, self.schedule_data_1["description"])

        self.assertEqual(schedule.step, self.schedule_data_1["step"])

    def test_create_schedule_using_user_medic(self):
    
        category = Category.objects.create(**self.category_data_1)

        specialty = Specialty.objects.create(**self.specialty_data_1)

        account = Account.objects.create_user(**self.account_data_1, is_medic=True)

        address_medic = Address.objects.create(**self.address_data_1)

        address_patient = Address.objects.create(**self.address_data_2)

        chart = Chart.objects.create(**self.chart_data_1)

        patient = Patient.objects.create(
            **self.patient_data_1,
            chart=chart,
            category=category,
            address=address_patient,
        )

        medic = Medic.objects.create(
            **self.medic_data_1,
            account=account,
            category=category,
            specialty=specialty,
            address=address_medic,
        )

        token = Token.objects.create(user=account)

        self.client.credentials(HTTP_AUTHORIZATION="Token " + token.key)

        response = self.client.post(
            f"/api/patient/{patient.id}/schedule/",
            {
                **self.schedule_data_1,
                "medic_id": medic.id,
                "patient_id": patient.id,
                "specialty_id": specialty.id,
            },
            format="json",
        )

        self.assertEqual(response.status_code, 403)

        responseJson = response.json()

        self.assertEqual(
            responseJson["detail"], "You do not have permission to perform this action."
        )

    def test_create_schedule_using_user_not_authenticated(self):
     
        category = Category.objects.create(**self.category_data_1)

        specialty = Specialty.objects.create(**self.specialty_data_1)

        account = Account.objects.create_user(**self.account_data_1, is_medic=True)

        address_medic = Address.objects.create(**self.address_data_1)

        address_patient = Address.objects.create(**self.address_data_2)

        chart = Chart.objects.create(**self.chart_data_1)

        patient = Patient.objects.create(
            **self.patient_data_1,
            chart=chart,
            category=category,
            address=address_patient,
        )

        medic = Medic.objects.create(
            **self.medic_data_1,
            account=account,
            category=category,
            specialty=specialty,
            address=address_medic,
        )

        response = self.client.post(
            f"/api/patient/{patient.id}/schedule/",
            {
                **self.schedule_data_1,
                "medic_id": medic.id,
                "patient_id": patient.id,
                "specialty_id": specialty.id,
            },
            format="json",
        )

        self.assertEqual(response.status_code, 401)

        responseJson = response.json()

        self.assertEqual(
            responseJson["detail"], "Authentication credentials were not provided."
        )   

    """ rota update """

    def test_update_schedule_using_user_admin(self):
        admin = Account.objects.create_superuser(**self.user_admin_data)
        token = Token.objects.create(user=admin)

        self.client.credentials(HTTP_AUTHORIZATION="Token " + token.key)

        category = Category.objects.create(**self.category_data_1)

        specialty = Specialty.objects.create(**self.specialty_data_1)

        account = Account.objects.create_user(**self.account_data_1, is_medic=True)

        address_medic = Address.objects.create(**self.address_data_1)

        address_patient = Address.objects.create(**self.address_data_2)

        chart = Chart.objects.create(**self.chart_data_1)

        patient = Patient.objects.create(
            **self.patient_data_1,
            chart=chart,
            category=category,
            address=address_patient,
        )

        medic = Medic.objects.create(
            **self.medic_data_1,
            account=account,
            category=category,
            specialty=specialty,
            address=address_medic,
        )

        schedule = Schedule.objects.create(
            **self.schedule_data_1,
            patient=patient,
            medic=medic,
            specialty=specialty,
        )

        self.assertEqual(schedule.completed, False)

        new_description = "nova descrição"

        response = self.client.patch(
            f"/api/patient/{patient.id}/schedule/{schedule.id}/",
            {
                "description": new_description
            },
            format="json",
        )

        self.assertEqual(response.status_code, 200)

        schedule = Schedule.objects.first()

        self.assertEqual(schedule.description, new_description)
    
    def test_update_schedule_using_user_employee(self):
        admin = Account.objects.create_user(**self.user_admin_data)
        token = Token.objects.create(user=admin)

        self.client.credentials(HTTP_AUTHORIZATION="Token " + token.key)

        category = Category.objects.create(**self.category_data_1)

        specialty = Specialty.objects.create(**self.specialty_data_1)

        account = Account.objects.create_user(**self.account_data_1, is_medic=True)

        address_medic = Address.objects.create(**self.address_data_1)

        address_patient = Address.objects.create(**self.address_data_2)

        chart = Chart.objects.create(**self.chart_data_1)

        patient = Patient.objects.create(
            **self.patient_data_1,
            chart=chart,
            category=category,
            address=address_patient,
        )

        medic = Medic.objects.create(
            **self.medic_data_1,
            account=account,
            category=category,
            specialty=specialty,
            address=address_medic,
        )

        schedule = Schedule.objects.create(
            **self.schedule_data_1,
            patient=patient,
            medic=medic,
            specialty=specialty,
        )

        new_description = "nova descrição"

        response = self.client.patch(
            f"/api/patient/{patient.id}/schedule/{schedule.id}/",
            {
                "description": new_description
            },
            format="json",
        )

        self.assertEqual(response.status_code, 200)

        schedule = Schedule.objects.first()

        self.assertEqual(schedule.description, new_description)

    def test_update_schedule_using_user_medic(self):
        
        category = Category.objects.create(**self.category_data_1)

        specialty = Specialty.objects.create(**self.specialty_data_1)

        account = Account.objects.create_user(**self.account_data_1, is_medic=True)

        address_medic = Address.objects.create(**self.address_data_1)

        address_patient = Address.objects.create(**self.address_data_2)

        chart = Chart.objects.create(**self.chart_data_1)

        patient = Patient.objects.create(
            **self.patient_data_1,
            chart=chart,
            category=category,
            address=address_patient,
        )

        medic = Medic.objects.create(
            **self.medic_data_1,
            account=account,
            category=category,
            specialty=specialty,
            address=address_medic,
        )

        schedule = Schedule.objects.create(
            **self.schedule_data_1,
            patient=patient,
            medic=medic,
            specialty=specialty,
        )

        token = Token.objects.create(user=account)

        self.client.credentials(HTTP_AUTHORIZATION="Token " + token.key)

        new_description = "nova descrição"

        response = self.client.patch(
            f"/api/patient/{patient.id}/schedule/{schedule.id}/",
            {
                "description": new_description
            },
            format="json",
        )

        self.assertEqual(response.status_code, 403)

        responseJson = response.json()

        self.assertEqual(
            responseJson["detail"], "You do not have permission to perform this action."
        )

    def test_update_schedule_using_user_not_authenticated(self):

        category = Category.objects.create(**self.category_data_1)

        specialty = Specialty.objects.create(**self.specialty_data_1)

        account = Account.objects.create_user(**self.account_data_1, is_medic=True)

        address_medic = Address.objects.create(**self.address_data_1)

        address_patient = Address.objects.create(**self.address_data_2)

        chart = Chart.objects.create(**self.chart_data_1)

        patient = Patient.objects.create(
            **self.patient_data_1,
            chart=chart,
            category=category,
            address=address_patient,
        )

        medic = Medic.objects.create(
            **self.medic_data_1,
            account=account,
            category=category,
            specialty=specialty,
            address=address_medic,
        )

        schedule = Schedule.objects.create(
            **self.schedule_data_1,
            patient=patient,
            medic=medic,
            specialty=specialty,
        )

        new_description = "nova descrição"

        response = self.client.patch(
            f"/api/patient/{patient.id}/schedule/{schedule.id}/",
            {
                "description": new_description
            },
            format="json",
        )

        self.assertEqual(response.status_code, 401)

        responseJson = response.json()

        self.assertEqual(
            responseJson["detail"], "Authentication credentials were not provided."
        )   

    """ rota getone """

    def test_getone_schedule_using_user_admin(self):
        admin = Account.objects.create_superuser(**self.user_admin_data)
        token = Token.objects.create(user=admin)

        self.client.credentials(HTTP_AUTHORIZATION="Token " + token.key)

        category = Category.objects.create(**self.category_data_1)

        specialty = Specialty.objects.create(**self.specialty_data_1)

        account = Account.objects.create_user(**self.account_data_1, is_medic=True)

        address_medic = Address.objects.create(**self.address_data_1)

        address_patient = Address.objects.create(**self.address_data_2)

        chart = Chart.objects.create(**self.chart_data_1)

        patient = Patient.objects.create(
            **self.patient_data_1,
            chart=chart,
            category=category,
            address=address_patient,
        )

        medic = Medic.objects.create(
            **self.medic_data_1,
            account=account,
            category=category,
            specialty=specialty,
            address=address_medic,
        )

        schedule = Schedule.objects.create(
            **self.schedule_data_1,
            patient=patient,
            medic=medic,
            specialty=specialty,
        )

        response = self.client.get(
            f"/api/patient/{patient.id}/schedule/{schedule.id}/",
        )

        self.assertEqual(response.status_code, 200)

        schedule = Schedule.objects.first()
    
    def test_getone_schedule_using_user_employee(self):
        admin = Account.objects.create_user(**self.user_admin_data)
        token = Token.objects.create(user=admin)

        self.client.credentials(HTTP_AUTHORIZATION="Token " + token.key)

        category = Category.objects.create(**self.category_data_1)

        specialty = Specialty.objects.create(**self.specialty_data_1)

        account = Account.objects.create_user(**self.account_data_1, is_medic=True)

        address_medic = Address.objects.create(**self.address_data_1)

        address_patient = Address.objects.create(**self.address_data_2)

        chart = Chart.objects.create(**self.chart_data_1)

        patient = Patient.objects.create(
            **self.patient_data_1,
            chart=chart,
            category=category,
            address=address_patient,
        )

        medic = Medic.objects.create(
            **self.medic_data_1,
            account=account,
            category=category,
            specialty=specialty,
            address=address_medic,
        )

        schedule = Schedule.objects.create(
            **self.schedule_data_1,
            patient=patient,
            medic=medic,
            specialty=specialty,
        )

        response = self.client.get(
            f"/api/patient/{patient.id}/schedule/{schedule.id}/",
        )

        self.assertEqual(response.status_code, 200)

        schedule = Schedule.objects.first()

    def test_getone_schedule_using_user_medic(self):
        
        category = Category.objects.create(**self.category_data_1)

        specialty = Specialty.objects.create(**self.specialty_data_1)

        account = Account.objects.create_user(**self.account_data_1, is_medic=True)

        address_medic = Address.objects.create(**self.address_data_1)

        address_patient = Address.objects.create(**self.address_data_2)

        chart = Chart.objects.create(**self.chart_data_1)

        patient = Patient.objects.create(
            **self.patient_data_1,
            chart=chart,
            category=category,
            address=address_patient,
        )

        medic = Medic.objects.create(
            **self.medic_data_1,
            account=account,
            category=category,
            specialty=specialty,
            address=address_medic,
        )

        schedule = Schedule.objects.create(
            **self.schedule_data_1,
            patient=patient,
            medic=medic,
            specialty=specialty,
        )

        token = Token.objects.create(user=account)

        self.client.credentials(HTTP_AUTHORIZATION="Token " + token.key)

        response = self.client.get(
            f"/api/patient/{patient.id}/schedule/{schedule.id}/",
        )

        self.assertEqual(response.status_code, 200)

        schedule = Schedule.objects.first()

    def test_getone_schedule_using_user_not_authenticated(self):

        category = Category.objects.create(**self.category_data_1)

        specialty = Specialty.objects.create(**self.specialty_data_1)

        account = Account.objects.create_user(**self.account_data_1, is_medic=True)

        address_medic = Address.objects.create(**self.address_data_1)

        address_patient = Address.objects.create(**self.address_data_2)

        chart = Chart.objects.create(**self.chart_data_1)

        patient = Patient.objects.create(
            **self.patient_data_1,
            chart=chart,
            category=category,
            address=address_patient,
        )

        medic = Medic.objects.create(
            **self.medic_data_1,
            account=account,
            category=category,
            specialty=specialty,
            address=address_medic,
        )

        schedule = Schedule.objects.create(
            **self.schedule_data_1,
            patient=patient,
            medic=medic,
            specialty=specialty,
        )

        response = self.client.get(
            f"/api/patient/{patient.id}/schedule/{schedule.id}/",
        )

        self.assertEqual(response.status_code, 401)

        responseJson = response.json()

        self.assertEqual(
            responseJson["detail"], "Authentication credentials were not provided."
        )   

    """ rota list consultas de um paciente """

    def test_list_patients_schedule_using_user_admin(self):
        admin = Account.objects.create_superuser(**self.user_admin_data)
        token = Token.objects.create(user=admin)

        self.client.credentials(HTTP_AUTHORIZATION="Token " + token.key)

        category = Category.objects.create(**self.category_data_1)

        specialty_1 = Specialty.objects.create(**self.specialty_data_1)

        specialty_2 = Specialty.objects.create(**self.specialty_data_2)

        account_1 = Account.objects.create_user(**self.account_data_1, is_medic=True)

        account_2 = Account.objects.create_user(**self.account_data_2, is_medic=True)

        address_medic_1 = Address.objects.create(**self.address_data_1)

        address_medic_2 = Address.objects.create(**self.address_data_1)

        address_patient = Address.objects.create(**self.address_data_2)

        chart = Chart.objects.create(**self.chart_data_1)

        patient = Patient.objects.create(
            **self.patient_data_1,
            chart=chart,
            category=category,
            address=address_patient,
        )

        medic_1 = Medic.objects.create(
            **self.medic_data_1,
            account=account_1,
            category=category,
            specialty=specialty_1,
            address=address_medic_1,
        )

        medic_2 = Medic.objects.create(
            **self.medic_data_2,
            account=account_2,
            category=category,
            specialty=specialty_2,
            address=address_medic_2,
        )

        Schedule.objects.create(
            **self.schedule_data_1,
            patient=patient,
            medic=medic_1,
            specialty=specialty_1,
        )

        Schedule.objects.create(
            **self.schedule_data_2,
            patient=patient,
            medic=medic_2,
            specialty=specialty_2,
        )

        response = self.client.get(
            f"/api/patient/{patient.id}/schedule/",
        )

        self.assertEqual(response.status_code, 200)

        responseJson = response.json()

        self.assertEqual(len(responseJson), 2)
    
    def test_list_patients_schedule_using_user_employee(self):
        admin = Account.objects.create_user(**self.user_admin_data)
        token = Token.objects.create(user=admin)

        self.client.credentials(HTTP_AUTHORIZATION="Token " + token.key)

        category = Category.objects.create(**self.category_data_1)

        specialty_1 = Specialty.objects.create(**self.specialty_data_1)

        specialty_2 = Specialty.objects.create(**self.specialty_data_2)

        account_1 = Account.objects.create_user(**self.account_data_1, is_medic=True)

        account_2 = Account.objects.create_user(**self.account_data_2, is_medic=True)

        address_medic_1 = Address.objects.create(**self.address_data_1)

        address_medic_2 = Address.objects.create(**self.address_data_1)

        address_patient = Address.objects.create(**self.address_data_2)

        chart = Chart.objects.create(**self.chart_data_1)

        patient = Patient.objects.create(
            **self.patient_data_1,
            chart=chart,
            category=category,
            address=address_patient,
        )

        medic_1 = Medic.objects.create(
            **self.medic_data_1,
            account=account_1,
            category=category,
            specialty=specialty_1,
            address=address_medic_1,
        )

        medic_2 = Medic.objects.create(
            **self.medic_data_2,
            account=account_2,
            category=category,
            specialty=specialty_2,
            address=address_medic_2,
        )

        Schedule.objects.create(
            **self.schedule_data_1,
            patient=patient,
            medic=medic_1,
            specialty=specialty_1,
        )

        Schedule.objects.create(
            **self.schedule_data_2,
            patient=patient,
            medic=medic_2,
            specialty=specialty_2,
        )

        response = self.client.get(
            f"/api/patient/{patient.id}/schedule/",
        )

        self.assertEqual(response.status_code, 200)

        responseJson = response.json()

        self.assertEqual(len(responseJson), 2)

    def test_list_patients_schedule_using_user_not_authenticated(self):
        
        category = Category.objects.create(**self.category_data_1)

        specialty_1 = Specialty.objects.create(**self.specialty_data_1)

        specialty_2 = Specialty.objects.create(**self.specialty_data_2)

        account_1 = Account.objects.create_user(**self.account_data_1, is_medic=True)

        account_2 = Account.objects.create_user(**self.account_data_2, is_medic=True)

        address_medic_1 = Address.objects.create(**self.address_data_1)

        address_medic_2 = Address.objects.create(**self.address_data_1)

        address_patient = Address.objects.create(**self.address_data_2)

        chart = Chart.objects.create(**self.chart_data_1)

        patient = Patient.objects.create(
            **self.patient_data_1,
            chart=chart,
            category=category,
            address=address_patient,
        )

        medic_1 = Medic.objects.create(
            **self.medic_data_1,
            account=account_1,
            category=category,
            specialty=specialty_1,
            address=address_medic_1,
        )

        medic_2 = Medic.objects.create(
            **self.medic_data_2,
            account=account_2,
            category=category,
            specialty=specialty_2,
            address=address_medic_2,
        )

        Schedule.objects.create(
            **self.schedule_data_1,
            patient=patient,
            medic=medic_1,
            specialty=specialty_1,
        )

        Schedule.objects.create(
            **self.schedule_data_2,
            patient=patient,
            medic=medic_2,
            specialty=specialty_2,
        )

        response = self.client.get(
            f"/api/patient/{patient.id}/schedule/",
        )

        self.assertEqual(response.status_code, 401)

        responseJson = response.json()

        self.assertEqual(
            responseJson["detail"], "Authentication credentials were not provided."
        )   

    """ rota list consultas de um medico """

    def test_list_medics_schedule_using_user_admin(self):
        admin = Account.objects.create_superuser(**self.user_admin_data)
        token = Token.objects.create(user=admin)

        self.client.credentials(HTTP_AUTHORIZATION="Token " + token.key)

        category = Category.objects.create(**self.category_data_1)

        specialty = Specialty.objects.create(**self.specialty_data_1)

        account = Account.objects.create_user(**self.account_data_1, is_medic=True)

        address_medic = Address.objects.create(**self.address_data_1)

        address_patient_1 = Address.objects.create(**self.address_data_1)

        address_patient_2 = Address.objects.create(**self.address_data_2)

        chart_1 = Chart.objects.create(**self.chart_data_1)

        chart_2 = Chart.objects.create(**self.chart_data_2)

        patient_1 = Patient.objects.create(
            **self.patient_data_1,
            chart=chart_1,
            category=category,
            address=address_patient_1,
        )

        patient_2 = Patient.objects.create(
            **self.patient_data_2,
            chart=chart_2,
            category=category,
            address=address_patient_2,
        )

        medic = Medic.objects.create(
            **self.medic_data_1,
            account=account,
            category=category,
            specialty=specialty,
            address=address_medic,
        )

        Schedule.objects.create(
            **self.schedule_data_1,
            patient=patient_1,
            medic=medic,
            specialty=specialty,
        )

        Schedule.objects.create(
            **self.schedule_data_2,
            patient=patient_2,
            medic=medic,
            specialty=specialty,
        )

        response = self.client.get(
            f"/api/medic/{medic.id}/schedule/",
        )

        self.assertEqual(response.status_code, 200)

        responseJson = response.json()

        self.assertEqual(len(responseJson), 2)
    
    def test_list_medics_schedule_using_user_employee(self):
        admin = Account.objects.create_user(**self.user_admin_data)
        token = Token.objects.create(user=admin)

        self.client.credentials(HTTP_AUTHORIZATION="Token " + token.key)

        category = Category.objects.create(**self.category_data_1)

        specialty = Specialty.objects.create(**self.specialty_data_1)

        account = Account.objects.create_user(**self.account_data_1, is_medic=True)

        address_medic = Address.objects.create(**self.address_data_1)

        address_patient_1 = Address.objects.create(**self.address_data_1)

        address_patient_2 = Address.objects.create(**self.address_data_2)

        chart_1 = Chart.objects.create(**self.chart_data_1)

        chart_2 = Chart.objects.create(**self.chart_data_2)

        patient_1 = Patient.objects.create(
            **self.patient_data_1,
            chart=chart_1,
            category=category,
            address=address_patient_1,
        )

        patient_2 = Patient.objects.create(
            **self.patient_data_2,
            chart=chart_2,
            category=category,
            address=address_patient_2,
        )

        medic = Medic.objects.create(
            **self.medic_data_1,
            account=account,
            category=category,
            specialty=specialty,
            address=address_medic,
        )

        Schedule.objects.create(
            **self.schedule_data_1,
            patient=patient_1,
            medic=medic,
            specialty=specialty,
        )

        Schedule.objects.create(
            **self.schedule_data_2,
            patient=patient_2,
            medic=medic,
            specialty=specialty,
        )

        response = self.client.get(
            f"/api/medic/{medic.id}/schedule/",
        )

        self.assertEqual(response.status_code, 200)

        responseJson = response.json()

        self.assertEqual(len(responseJson), 2)

    def test_list_medics_schedule_using_user_medic(self):
        
        category = Category.objects.create(**self.category_data_1)

        specialty = Specialty.objects.create(**self.specialty_data_1)

        account = Account.objects.create_user(**self.account_data_1, is_medic=True)

        address_medic = Address.objects.create(**self.address_data_1)

        address_patient_1 = Address.objects.create(**self.address_data_1)

        address_patient_2 = Address.objects.create(**self.address_data_2)

        chart_1 = Chart.objects.create(**self.chart_data_1)

        chart_2 = Chart.objects.create(**self.chart_data_2)

        patient_1 = Patient.objects.create(
            **self.patient_data_1,
            chart=chart_1,
            category=category,
            address=address_patient_1,
        )

        patient_2 = Patient.objects.create(
            **self.patient_data_2,
            chart=chart_2,
            category=category,
            address=address_patient_2,
        )

        medic = Medic.objects.create(
            **self.medic_data_1,
            account=account,
            category=category,
            specialty=specialty,
            address=address_medic,
        )

        Schedule.objects.create(
            **self.schedule_data_1,
            patient=patient_1,
            medic=medic,
            specialty=specialty,
        )

        Schedule.objects.create(
            **self.schedule_data_2,
            patient=patient_2,
            medic=medic,
            specialty=specialty,
        )

        token = Token.objects.create(user=account)

        self.client.credentials(HTTP_AUTHORIZATION="Token " + token.key)

        response = self.client.get(
            f"/api/medic/{medic.id}/schedule/",
        )

        self.assertEqual(response.status_code, 200)

        responseJson = response.json()

        self.assertEqual(len(responseJson), 2)

    def test_list_medics_schedule_using_user_not_authenticated(self):
        
        category = Category.objects.create(**self.category_data_1)

        specialty = Specialty.objects.create(**self.specialty_data_1)

        account = Account.objects.create_user(**self.account_data_1, is_medic=True)

        address_medic = Address.objects.create(**self.address_data_1)

        address_patient_1 = Address.objects.create(**self.address_data_1)

        address_patient_2 = Address.objects.create(**self.address_data_2)

        chart_1 = Chart.objects.create(**self.chart_data_1)

        chart_2 = Chart.objects.create(**self.chart_data_2)

        patient_1 = Patient.objects.create(
            **self.patient_data_1,
            chart=chart_1,
            category=category,
            address=address_patient_1,
        )

        patient_2 = Patient.objects.create(
            **self.patient_data_2,
            chart=chart_2,
            category=category,
            address=address_patient_2,
        )

        medic = Medic.objects.create(
            **self.medic_data_1,
            account=account,
            category=category,
            specialty=specialty,
            address=address_medic,
        )

        Schedule.objects.create(
            **self.schedule_data_1,
            patient=patient_1,
            medic=medic,
            specialty=specialty,
        )

        Schedule.objects.create(
            **self.schedule_data_2,
            patient=patient_2,
            medic=medic,
            specialty=specialty,
        )

        response = self.client.get(
            f"/api/medic/{medic.id}/schedule/",
        )

        self.assertEqual(response.status_code, 401)

        responseJson = response.json()

        self.assertEqual(
            responseJson["detail"], "Authentication credentials were not provided."
        )   

    """ rota delete """

    def test_delete_schedule_using_user_admin(self):
        admin = Account.objects.create_superuser(**self.user_admin_data)
        token = Token.objects.create(user=admin)

        self.client.credentials(HTTP_AUTHORIZATION="Token " + token.key)

        category = Category.objects.create(**self.category_data_1)

        specialty = Specialty.objects.create(**self.specialty_data_1)

        account = Account.objects.create_user(**self.account_data_1, is_medic=True)

        address_medic = Address.objects.create(**self.address_data_1)

        address_patient = Address.objects.create(**self.address_data_2)

        chart = Chart.objects.create(**self.chart_data_1)

        patient = Patient.objects.create(
            **self.patient_data_1,
            chart=chart,
            category=category,
            address=address_patient,
        )

        medic = Medic.objects.create(
            **self.medic_data_1,
            account=account,
            category=category,
            specialty=specialty,
            address=address_medic,
        )

        schedule = Schedule.objects.create(
            **self.schedule_data_1,
            patient=patient,
            medic=medic,
            specialty=specialty,
        )

        response = self.client.delete(
            f"/api/patient/{patient.id}/schedule/{schedule.id}/cancel/",
        )

        self.assertEqual(response.status_code, 204)
    
    def test_delete_schedule_using_user_employee(self):
        admin = Account.objects.create_user(**self.user_admin_data)
        token = Token.objects.create(user=admin)

        self.client.credentials(HTTP_AUTHORIZATION="Token " + token.key)

        category = Category.objects.create(**self.category_data_1)

        specialty = Specialty.objects.create(**self.specialty_data_1)

        account = Account.objects.create_user(**self.account_data_1, is_medic=True)

        address_medic = Address.objects.create(**self.address_data_1)

        address_patient = Address.objects.create(**self.address_data_2)

        chart = Chart.objects.create(**self.chart_data_1)

        patient = Patient.objects.create(
            **self.patient_data_1,
            chart=chart,
            category=category,
            address=address_patient,
        )

        medic = Medic.objects.create(
            **self.medic_data_1,
            account=account,
            category=category,
            specialty=specialty,
            address=address_medic,
        )

        schedule = Schedule.objects.create(
            **self.schedule_data_1,
            patient=patient,
            medic=medic,
            specialty=specialty,
        )

        response = self.client.delete(
            f"/api/patient/{patient.id}/schedule/{schedule.id}/cancel/",
        )

        self.assertEqual(response.status_code, 204)

        """ responseJson = response.json()

        self.assertEqual(
            responseJson["detail"], "You do not have permission to perform this action."
        ) """

    def test_delete_schedule_using_user_medic(self):

        category = Category.objects.create(**self.category_data_1)

        specialty = Specialty.objects.create(**self.specialty_data_1)

        account = Account.objects.create_user(**self.account_data_1, is_medic=True)

        address_medic = Address.objects.create(**self.address_data_1)

        address_patient = Address.objects.create(**self.address_data_2)

        chart = Chart.objects.create(**self.chart_data_1)

        patient = Patient.objects.create(
            **self.patient_data_1,
            chart=chart,
            category=category,
            address=address_patient,
        )

        medic = Medic.objects.create(
            **self.medic_data_1,
            account=account,
            category=category,
            specialty=specialty,
            address=address_medic,
        )

        schedule = Schedule.objects.create(
            **self.schedule_data_1,
            patient=patient,
            medic=medic,
            specialty=specialty,
        )

        token = Token.objects.create(user=account)

        self.client.credentials(HTTP_AUTHORIZATION="Token " + token.key)

        response = self.client.delete(
            f"/api/patient/{patient.id}/schedule/{schedule.id}/cancel/",
        )

        self.assertEqual(response.status_code, 403)

        responseJson = response.json()

        self.assertEqual(
            responseJson["detail"], "You do not have permission to perform this action."
        )

    def test_delete_schedule_using_user_not_authenticated(self):

        category = Category.objects.create(**self.category_data_1)

        specialty = Specialty.objects.create(**self.specialty_data_1)

        account = Account.objects.create_user(**self.account_data_1, is_medic=True)

        address_medic = Address.objects.create(**self.address_data_1)

        address_patient = Address.objects.create(**self.address_data_2)

        chart = Chart.objects.create(**self.chart_data_1)

        patient = Patient.objects.create(
            **self.patient_data_1,
            chart=chart,
            category=category,
            address=address_patient,
        )

        medic = Medic.objects.create(
            **self.medic_data_1,
            account=account,
            category=category,
            specialty=specialty,
            address=address_medic,
        )

        schedule = Schedule.objects.create(
            **self.schedule_data_1,
            patient=patient,
            medic=medic,
            specialty=specialty,
        )

        response = self.client.delete(
            f"/api/patient/{patient.id}/schedule/{schedule.id}/cancel/",
        )

        self.assertEqual(response.status_code, 401)

        responseJson = response.json()

        self.assertEqual(
            responseJson["detail"], "Authentication credentials were not provided."
        )   
