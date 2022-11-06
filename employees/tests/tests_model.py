from django.test import TestCase
from employees.models import Employee
from addresses.models import Address
from accounts.models import Account
from django.db import IntegrityError


class EmployeeModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):

        cls.address_data = {
            "street": "rua para teste",
            "number": 20,
            "cep": "12355687",
            "state": "rn",
            "district": "mohgw",
            "city": "cidade teste",
        }
        cls.address = Address.objects.create(**cls.address_data)

        cls.account_data = {
            "first_name": "gabri",
            "last_name": "ela",
            "username": "gabrieularyssa",
            "phone_number": "888888",
            "is_medic": False,
        }
        cls.account = Account.objects.create_user(**cls.account_data)

        cls.employee_data = {
            "cpf": "102152465432",
        }

        cls.employee = Employee.objects.create(
            **cls.employee_data, account=cls.account, address=cls.address)

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


class EmployeeRelationshipsTest(TestCase):
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
            "password": "sdada11231"
        }

        cls.employee_data = {
            "cpf": "12312312315",
        }

        cls.account = Account.objects.create_user(**cls.account_data)
        cls.address = Address.objects.create(**cls.address_data)
        cls.employee = Employee.objects.create(
            **cls.employee_data, account=cls.account, address=cls.address)

    def test_if_employee_can_have_an_address(self):
        # Verifica se um employee pode registrar um address relacionado

        self.assertIs(self.address.employees, self.employee)

        self.assertIs(self.address, self.employee.address)

    def test_if_employee_can_have_an_account(self):
        # Verifica se um funcionário pode ter somente uma account relacionada

        self.assertIs(self.account.employees, self.employee)

        self.assertIs(self.account, self.employee.account)

    def test_if_raise_error_when_employee_already_have_an_address(self):
        """ Verifica se um erro é levantado ao atribuir o mesmo address a 
        outro employee """

        with self.assertRaises(IntegrityError):
            account_two_data = {
                "first_name": "fulano",
                "last_name": "de tal",
                "phone_number": "12345565565",
                "username": "hilary",
                "password": "sdada11231"
            }

            employee_two_data = {
                "cpf": "12312312319",
            }

            account = Account.objects.create_user(**account_two_data)
            employee_two = Employee.objects.create(
                **employee_two_data, account=account, address=self.address)

    def test_if_raise_error_when_employee_already_have_an_account(self):
        """ Verifica se um erro é levantado ao atribuir a mesma account a 
        outro employee """

        with self.assertRaises(IntegrityError):
            address_two_data = {
                "street": "rua das magueiras",
                "number": 100,
                "cep": "12345656",
                "state": "SP",
                "district": "bairro lalala",
                "city": "São Paulo",
            }

            employee_two_data = {
                "cpf": "12312312329",
            }

            address = Address.objects.create(**address_two_data)
            employee_two = Employee.objects.create(
                **employee_two_data, account=self.account, address=address)
