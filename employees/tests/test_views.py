from rest_framework.test import APITestCase
from rest_framework.views import status
from rest_framework.authtoken.models import Token
from accounts.models import Account
from employees.models import Employee
from addresses.models import Address


class create_employee_test(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.register_url = "/api/employee/"
        cls.employee_data = {
            "cpf": "12312312315",
        }
        cls.address_data = {
            "street": "rua das magueiras",
            "number": 100,
            "cep": "12345656",
            "state": "SP",
            "district": "bairro lalala",
            "city": "São Paulo",
        }

        cls.account_data = {
            "first_name": "fulanoo",
            "last_name": "de tal",
            "phone_number": "12345565565",
            "username": "hillarianey",
            "password": "sdada11231",
        }

        cls.user_admin_data = {
            "first_name": "admin",
            "last_name": "admin",
            "phone_number": "777777777777",
            "username": "admins",
            "password": "admin",
            "is_medic": False,
        }

    def test_create_employee_fail(self):
        """
        Verificar criação de employee sem autenticação
        """
        response = self.client.post(self.register_url, self.employee_data)

        expected_status_code = status.HTTP_401_UNAUTHORIZED
        result_status_code = response.status_code

        self.assertEqual(expected_status_code, result_status_code)

    def test_create_employee(self):
        """
        Verifica se o admin pode criar uma employee
        """
        admin = Account.objects.create_superuser(**self.user_admin_data)
        token = Token.objects.create(user=admin)
        self.client.credentials(HTTP_AUTHORIZATION="Token " + token.key)

        response = self.client.post(
            self.register_url,
            {
                **self.employee_data,
                "address": self.address_data,
                "account": self.account_data,
            },
            format="json",
        )
        self.assertEqual(response.status_code, 201)

        employee = Employee.objects.first()

        self.assertEqual(self.employee_data["cpf"], employee.cpf)

        self.assertEqual(self.address_data["street"], employee.address.street)
        self.assertEqual(self.address_data["number"], employee.address.number)
        self.assertEqual(self.address_data["cep"], employee.address.cep)
        self.assertEqual(self.address_data["state"], employee.address.state)
        self.assertEqual(self.address_data["district"], employee.address.district)

        self.assertEqual(self.account_data["first_name"], employee.account.first_name)
        self.assertEqual(self.account_data["last_name"], employee.account.last_name)
        self.assertEqual(
            self.account_data["phone_number"], employee.account.phone_number
        )
        self.assertEqual(self.account_data["username"], employee.account.username)
        self.assertEqual(False, employee.account.is_superuser)
