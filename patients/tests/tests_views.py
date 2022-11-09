from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from patients.models import Patient
from addresses.models import Address
from categories.models import Category
from charts.models import Chart
from accounts.models import Account


class PatientsViewTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user_admin_data = {
            "first_name": "admin",
            "last_name": "admin",
            "phone_number": "777777777777",
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

        cls.category_data_2 = {"color": "red2", "description": "lalalala2"}

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

    def test_create_patients_using_user_authenticated(self):
        admin = Account.objects.create_superuser(**self.user_admin_data)
        token = Token.objects.create(user=admin)

        self.client.credentials(HTTP_AUTHORIZATION="Token " + token.key)

        category = Category.objects.create(**self.category_data_1)

        response = self.client.post(
            "/api/patient/",
            {
                **self.patient_data_1,
                "address": self.address_data_1,
                "chart": self.chart_data_1,
                "category_id": category.id,
            },
            format="json",
        )

        self.assertEqual(response.status_code, 201)

        patient = Patient.objects.first()

        self.assertEqual(self.patient_data_1["first_name"], patient.first_name)
        self.assertEqual(self.patient_data_1["last_name"], patient.last_name)
        self.assertEqual(self.patient_data_1["cpf"], patient.cpf)

        self.assertEqual(self.address_data_1["street"], patient.address.street)
        self.assertEqual(self.address_data_1["number"], patient.address.number)
        self.assertEqual(self.address_data_1["cep"], patient.address.cep)
        self.assertEqual(self.address_data_1["state"], patient.address.state)
        self.assertEqual(self.address_data_1["district"], patient.address.district)

        self.assertEqual(self.chart_data_1["is_pregnant"], patient.chart.is_pregnant)
        self.assertEqual(self.chart_data_1["is_diabetic"], patient.chart.is_diabetic)
        self.assertEqual(self.chart_data_1["is_smoker"], patient.chart.is_smoker)
        self.assertEqual(self.chart_data_1["is_allergic"], patient.chart.is_allergic)
        self.assertEqual(self.chart_data_1["heart_disease"], patient.chart.heart_disease)
        self.assertEqual(self.chart_data_1["dificulty_healing"], patient.chart.dificulty_healing)
        self.assertEqual(self.chart_data_1["use_medication"], patient.chart.use_medication)
        self.assertEqual(self.chart_data_1["other_information"], patient.chart.other_information)

        self.assertEqual(category.id, patient.category.id)

    def test_create_patients_using_user_not_authenticated(self):
        category = Category.objects.create(**self.category_data_1)

        response = self.client.post(
            "/api/patient/",
            {
                **self.patient_data_1,
                "address": self.address_data_1,
                "chart": self.chart_data_1,
                "category_id": category.id,
            },
            format="json",
        )

        self.assertEqual(response.status_code, 401)

        responseJson = response.json()

        self.assertEqual(
            responseJson["detail"], "Authentication credentials were not provided."
        )

    def test_update_patients_using_user_authenticated(self):
        admin = Account.objects.create_superuser(**self.user_admin_data)
        token = Token.objects.create(user=admin)

        self.client.credentials(HTTP_AUTHORIZATION="Token " + token.key)

        category_1 = Category.objects.create(**self.category_data_1)

        category_2 = Category.objects.create(**self.category_data_2)

        address = Address.objects.create(**self.address_data_1)

        chart = Chart.objects.create(**self.chart_data_1)

        patient = Patient.objects.create(
            **self.patient_data_1,
            chart=chart,
            category=category_1,
            address=address,
        )

        response = self.client.patch(
            f"/api/patient/{patient.id}/",
            {
                **self.patient_data_1,
                "chart": self.chart_data_2,
                "category_id": category_2.id,
            },
            format="json",
        )

        self.assertEqual(response.status_code, 200)

        patient = Patient.objects.get(id=patient.id)

        self.assertEqual(self.patient_data_1["first_name"], patient.first_name)
        self.assertEqual(self.patient_data_1["last_name"], patient.last_name)
        self.assertEqual(self.patient_data_1["cpf"], patient.cpf)

        self.assertEqual(self.chart_data_1["is_pregnant"], patient.chart.is_pregnant)
        self.assertEqual(self.chart_data_1["is_diabetic"], patient.chart.is_diabetic)
        self.assertEqual(self.chart_data_1["is_smoker"], patient.chart.is_smoker)
        self.assertEqual(self.chart_data_1["is_allergic"], patient.chart.is_allergic)
        self.assertEqual(self.chart_data_1["heart_disease"], patient.chart.heart_disease)
        self.assertEqual(self.chart_data_1["dificulty_healing"], patient.chart.dificulty_healing)
        self.assertEqual(self.chart_data_1["use_medication"], patient.chart.use_medication)
        self.assertEqual(self.chart_data_1["other_information"], patient.chart.other_information)

        self.assertEqual(category_2.id, patient.category.id)

    def test_update_patients_using_user_not_authenticated(self):
        
        category_1 = Category.objects.create(**self.category_data_1)

        category_2 = Category.objects.create(**self.category_data_2)

        address = Address.objects.create(**self.address_data_1)

        chart = Chart.objects.create(**self.chart_data_1)

        patient = Patient.objects.create(
            **self.patient_data_1,
            chart=chart,
            category=category_1,
            address=address,
        )

        response = self.client.patch(
            f"/api/patient/{patient.id}/",
            {
                **self.patient_data_1,
                "chart": self.chart_data_2,
                "category_id": category_2.id,
            },
            format="json",
        )

        self.assertEqual(response.status_code, 401)

        responseJson = response.json()

        self.assertEqual(
            responseJson["detail"], "Authentication credentials were not provided."
        )    

    def test_list_patients_using_user_authenticated(self):

        admin = Account.objects.create_superuser(**self.user_admin_data)
        token = Token.objects.create(user=admin)

        self.client.credentials(HTTP_AUTHORIZATION="Token " + token.key)

        category_1 = Category.objects.create(**self.category_data_1)

        category_2 = Category.objects.create(**self.category_data_2)

        address_1 = Address.objects.create(**self.address_data_1)

        address_2 = Address.objects.create(**self.address_data_2)

        chart_1 = Chart.objects.create(**self.chart_data_1)

        chart_2 = Chart.objects.create(**self.chart_data_2)

        Patient.objects.create(
            **self.patient_data_1,
            chart=chart_1,
            category=category_1,
            address=address_1,
        )

        Patient.objects.create(
            **self.patient_data_2,
            chart=chart_2,
            category=category_2,
            address=address_2,
        )

        response = self.client.get("/api/patient/")

        self.assertEqual(response.status_code, 200)

        responseJson = response.json()

        self.assertEqual(len(responseJson), 2)

    def test_list_patients_using_user_not_authenticated(self):

        category_1 = Category.objects.create(**self.category_data_1)

        category_2 = Category.objects.create(**self.category_data_2)

        address_1 = Address.objects.create(**self.address_data_1)

        address_2 = Address.objects.create(**self.address_data_2)

        chart_1 = Chart.objects.create(**self.chart_data_1)

        chart_2 = Chart.objects.create(**self.chart_data_2)

        Patient.objects.create(
            **self.patient_data_1,
            chart=chart_1,
            category=category_1,
            address=address_1,
        )

        Patient.objects.create(
            **self.patient_data_2,
            chart=chart_2,
            category=category_2,
            address=address_2,
        )

        response = self.client.get("/api/patient/")

        self.assertEqual(response.status_code, 401)

        responseJson = response.json()

        self.assertEqual(
            responseJson["detail"], "Authentication credentials were not provided."
        )    

    def test_getone_patients_using_user_authenticated(self):
        admin = Account.objects.create_superuser(**self.user_admin_data)
        token = Token.objects.create(user=admin)

        self.client.credentials(HTTP_AUTHORIZATION="Token " + token.key)

        category = Category.objects.create(**self.category_data_1)

        address = Address.objects.create(**self.address_data_1)

        chart = Chart.objects.create(**self.chart_data_1)

        patient = Patient.objects.create(
            **self.patient_data_1,
            chart=chart,
            category=category,
            address=address,
        )

        response = self.client.get(f"/api/patient/{patient.id}/")

        self.assertEqual(response.status_code, 200)

        responseJson = response.json()

        self.assertEqual(self.patient_data_1["first_name"], responseJson["first_name"])
        self.assertEqual(self.patient_data_1["last_name"], responseJson["last_name"])
        self.assertEqual(self.patient_data_1["cpf"], responseJson["cpf"])

        self.assertEqual(self.address_data_1["street"], responseJson["address"]["street"])
        self.assertEqual(self.address_data_1["number"], responseJson["address"]["number"])
        self.assertEqual(self.address_data_1["cep"], responseJson["address"]["cep"])
        self.assertEqual(self.address_data_1["state"], responseJson["address"]["state"])
        self.assertEqual(self.address_data_1["district"], responseJson["address"]["district"])

        self.assertEqual(self.chart_data_1["is_pregnant"], responseJson["chart"]["is_pregnant"])
        self.assertEqual(self.chart_data_1["is_diabetic"], responseJson["chart"]["is_diabetic"])
        self.assertEqual(self.chart_data_1["is_smoker"], responseJson["chart"]["is_smoker"])
        self.assertEqual(self.chart_data_1["is_allergic"], responseJson["chart"]["is_allergic"])
        self.assertEqual(self.chart_data_1["heart_disease"], responseJson["chart"]["heart_disease"])
        self.assertEqual(self.chart_data_1["dificulty_healing"], responseJson["chart"]["dificulty_healing"])
        self.assertEqual(self.chart_data_1["use_medication"], responseJson["chart"]["use_medication"])
        self.assertEqual(self.chart_data_1["other_information"], responseJson["chart"]["other_information"])

    def test_getone_patients_using_user_not_authenticated(self):
        
        category = Category.objects.create(**self.category_data_1)

        address = Address.objects.create(**self.address_data_1)

        chart = Chart.objects.create(**self.chart_data_1)

        patient = Patient.objects.create(
            **self.patient_data_1,
            chart=chart,
            category=category,
            address=address,
        )

        response = self.client.get(f"/api/patient/{patient.id}/")

        self.assertEqual(response.status_code, 401)

        responseJson = response.json()

        self.assertEqual(
            responseJson["detail"], "Authentication credentials were not provided."
        )

    def test_delete_patients_using_user_admin(self):
        admin = Account.objects.create_superuser(**self.user_admin_data)
        token = Token.objects.create(user=admin)

        self.client.credentials(HTTP_AUTHORIZATION="Token " + token.key)

        category = Category.objects.create(**self.category_data_1)

        address = Address.objects.create(**self.address_data_1)

        chart = Chart.objects.create(**self.chart_data_1)

        patient = Patient.objects.create(
            **self.patient_data_1,
            chart=chart,
            category=category,
            address=address,
        )

        response = self.client.delete(f"/api/patient/{patient.id}/")

        self.assertEqual(response.status_code, 204)

        self.assertEqual(len(Patient.objects.all()), 0)

    def test_delete_patients_using_other_user(self):
        admin = Account.objects.create_user(**self.user_admin_data)
        token = Token.objects.create(user=admin)

        self.client.credentials(HTTP_AUTHORIZATION="Token " + token.key)

        category = Category.objects.create(**self.category_data_1)

        address = Address.objects.create(**self.address_data_1)

        chart = Chart.objects.create(**self.chart_data_1)

        patient = Patient.objects.create(
            **self.patient_data_1,
            chart=chart,
            category=category,
            address=address,
        )

        response = self.client.delete(f"/api/patient/{patient.id}/")

        self.assertEqual(response.status_code, 403)

        responseJson = response.json()

        self.assertEqual(
            responseJson["detail"], "You do not have permission to perform this action."
        )
