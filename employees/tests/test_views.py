from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from rest_framework.views import status
from accounts.models import Account
from employees.models import Employee
from addresses.models import Address
from rest_framework.test import APIClient
from rest_framework.test import APITestCase
from rest_framework.views import status

# client = APIClient()

# response_get = client.get("/api/employee/")

# response_post = client.post(
#     "/api/employee/",
#     {
#         "account": {
#             "first_name": "Valeria",
#             "last_name": "Silva",
#             "phone_number": "12345565565",
#             "is_medic": False,
#             "username": "Vava",
#             "password": "1234",
#         },
#         "cpf": "123456528",
#         "address": {
#             "street": "rua das magueiras",
#             "number": 2147,
#             "cep": "1234568",
#             "state": "BH",
#             "district": "Bandeirantes",
#             "city": "Minas",
#         },
#     },
#     format="json",
# )


# class LibrarianRegisterViewTest(APITestCase):
#     @classmethod
#     def setUpTestData(cls) -> None:
#         cls.register_url = "/api/employee/"
#         cls.librarian_data = {
#             "account": {
#                 "first_name": "Valeria",
#                 "last_name": "Silva",
#                 "phone_number": "123455565",
#                 "is_medic": False,
#                 "username": "Va",
#                 "password": "1234",
#             },
#             "cpf": "123456528",
#             "address": {
#                 "street": "rua das magueiras",
#                 "number": 2147,
#                 "cep": "1234568",
#                 "state": "BH",
#                 "district": "Bandeirantes",
#                 "city": "Minas",
#             },
#         }

#     def test_can_register_librarian(self):

#         user = Account.objects.create_user(**self.user_vendedor_data)

#         token = Token.objects.create(user=user)

#         self.client.credentials(HTTP_AUTHORIZATION="Token " + token.key)

#         response = self.client.post(
#             self.register_url, self.librarian_data, format="json"
#         )
#         # ipdb.set_trace()
#         # print()

#         # expected_status_code = 201
#         expected_status_code = status.HTTP_201_CREATED
#         result_status_code = response.status_code

#         self.assertEqual(expected_status_code, result_status_code)


# class EmployeeLoginViewTest(APITestCase):
#     @classmethod
#     def setUpTestData(cls) -> None:
#         cls.cadastrar_url = "/api/employee/"
#         cls.login_url = "/api/login/"
#         cls.register_data = {
#             "account": {
#                 "first_name": "Valeria",
#                 "last_name": "Silva",
#                 "phone_number": "12345565565",
#                 "is_medic": False,
#                 "username": "Vava",
#                 "password": "1234",
#             },
#             "cpf": "123456528",
#             "address": {
#                 "street": "rua das magueiras",
#                 "number": 2147,
#                 "cep": "1234568",
#                 "state": "BH",
#                 "district": "Bandeirantes",
#                 "city": "Minas",
#             },
#         }
#         cls.account_data = {
#             "first_name": "Valeria",
#             "last_name": "Silva",
#             "username": "Drika",
#             "phone_number": "21947852540",
#             "is_medic": False,
#         }

#     def test_can_login_account(self):
#         register_response = self.client.post(
#             self.cadastrar_url, self.register_data, format="json"
#         )
#         login_response = self.client.post(self.login_url, self.account_data)

#         expected_status_code = status.HTTP_200_OK
#         result_status_code = login_response.status_code

#         self.assertEqual(expected_status_code, result_status_code)


# class EmployeeRegisterViewTest(APITestCase):
#     @classmethod
#     def setUpTestData(cls) -> None:
#         cls.register_url = "/api/employee/"
#         cls.register_data = {
#             "account": {
#                 "first_name": "Valeria",
#                 "last_name": "Silva",
#                 "phone_number": "12345565565",
#                 "is_medic": False,
#                 "username": "Vava",
#                 "password": "1234",
#             },
#             "cpf": "123456528",
#             "address": {
#                 "street": "rua das magueiras",
#                 "number": 2147,
#                 "cep": "1234568",
#                 "state": "BH",
#                 "district": "Bandeirantes",
#                 "city": "Minas",
#             },
#         }
#         # cls.account_data = {
#         #     "first_name": "Valeria",
#         #     "last_name": "Silva",
#         #     "username": "Drika",
#         #     "phone_number": "21947852540",
#         #     "is_medic": False,
#         # }

#     def test_can_regster_account(self):
#         response = self.client.post(self.register_url, self.account_data)

#         expected_status_code = status.HTTP_201_CREATED
#         result_status_code = response.status_code

#         self.assertEqual(expected_status_code, result_status_code)


# class EmployeesViewTest(APITestCase):
#     @classmethod
#     def setUpTestData(cls):
#         cls.employee_data = {
#             "cpf": "12457896325",
#             "address": 1,
#             "account": 1,
#         }

#         cls.employee_data_2 = {
#             "cpf": "12457896325",
#             "address": 2,
#             "account": 2,
#         }

#         cls.address_data = {
#             "street": "Rua Oliveira",
#             "number": 35,
#             "cep": "24890587",
#             "state": "MG",
#             "district": "Bandeirantes",
#         }

#         cls.address_data_2 = {
#             "street": "Rua Oliveira",
#             "number": 35,
#             "cep": "24890587",
#             "state": "MG",
#             "district": "Bandeirantes",
#         }

#         # cls.product_update_data = {
#         #     "description": "Smartband XYZ 77.0",
#         # }

#         cls.account_data = {
#             "first_name": "Adriana",
#             "last_name": "Silva",
#             "username": "Drika",
#             "phone_number": "21947852540",
#             "is_medic": False,
#         }

#         cls.account_data_2 = {
#             "first_name": "Anderson",
#             "last_name": "Silva",
#             "username": "Anderson7",
#             "phone_number": "21947852541",
#             "is_medic": False,
#         }

#         # cls.user_nao_vendedor_data = {
#         #     "username": "anderson3",
#         #     "password": "1234",
#         #     "first_name": "Anderson3",
#         #     "last_name": "Alves",
#         #     "is_seller": False,
#         # }

#         # cls.super_user_data = {
#         #     "username": "anderson8",
#         #     "password": "1234",
#         #     "first_name": "Anderson8",
#         #     "last_name": "Alves",
#         #     "is_seller": False,
#         # }
#   def test_can_login_account(self):
# #         register_response = self.client.post(
# #             self.cadastrar_url, self.register_data, format="json"
# #         )
# #         login_response = self.client.post(self.login_url, self.account_data)

# #         expected_status_code = status.HTTP_200_OK
# #         result_status_code = login_response.status_code

# #         self.assertEqual(expected_status_code, result_status_code)
#     # def test_criacao_employee(self):
#     #     """usuário admin cadastrando employee"""
#     #     user = Account.objects.create_user(**self.account_data)

#     #     token = Token.objects.create(user=user)

#     #     self.client.credentials(HTTP_AUTHORIZATION="Token " + token.key)

#     #     response = self.client.post(
#     #         "/api/employee/",
#     #         self.employee_data,
#     #         format="json",
#     #     )

#     #     self.assertEqual(response.status_code, 201)

#     #     employee = Employee.objects.first()

#     #     self.assertEqual(self.employee.cpf, self.employee_data["cpf"])
#     #     self.assertEqual(self.employee.address, self.employee_data["address"])
#     #     self.assertEqual(self.employee.account, self.employee_data["account"])


class EmployeeRegisterViewTest(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.register_url = "/api/employee/"
        cls.employee_data = {
            "account": {
                "first_name": "Valeria",
                "last_name": "Silva",
                "phone_number": "123455565",
                "is_medic": False,
                "username": "Va",
                "password": "1234",
            },
            "cpf": "123456528",
            "address": {
                "street": "rua das magueiras",
                "number": 2147,
                "cep": "1234568",
                "state": "BH",
                "district": "Bandeirantes",
                "city": "Minas",
            },
        }

    def test_can_register(self):
        response = self.client.post(self.register_url, self.employee_data, format="json")
        # ipdb.set_trace()
        # print()

        # expected_status_code = 201
        expected_status_code = status.HTTP_201_CREATED
        result_status_code = response.status_code

        self.assertEqual(expected_status_code, result_status_code)
