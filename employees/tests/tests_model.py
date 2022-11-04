from django.test import TestCase
from employees.models import Employee
from addresses.models import Address
from accounts.models import Account


class EmployeeModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):

        cls.employee_data = {
            "cpf": "102152465432",
            "account_id": 1,
            "address_id": 1,
        }

        cls.employee = Employee.objects.create(
            **cls.employee_data,
        )

        cls.address_data = {
            "street": "rua para teste",
            "number": 20,
            "cep": "12355687",
            "state": "rn",
            "district": "mohgw",
        }
        cls.address = Address.objects.create(**cls.address_data)

        cls.account_data = {
            "first_name": "gabri",
            "last_name": "ela",
            "username": "gabrieularyssa",
            "phone_number": "888888",
            "is_medic": False,
        }
        cls.account = Account.objects.create(**cls.account_data)

    def test_employee(self):
        """
        Verifica se cpf esta sendo persistido como cpf
        """
        self.assertEqual(self.employee.cpf, self.employee_data["cpf"])

    def test_employee_max_length_cpf(self):
        """
        Verifica o max_length do cpf
        """
        expected_max_length = 14
        result_max_length = Employee._meta.get_field("cpf").max_length
        self.assertEqual(expected_max_length, result_max_length)
