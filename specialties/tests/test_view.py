# tentar criar especialidade com o is_medic false
# criar especialidade com o is_medic true
from rest_framework.test import APITestCase
from rest_framework.views import status
from rest_framework.authtoken.models import Token
from accounts.models import Account


class create_specialty_test(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.register_url = "/api/specialty/"
        cls.specialty_data = {
            "name": "otorrino",
        }
        cls.account_data = {
            "first_name": "gabriela",
            "last_name": "oliveira",
            "username": "gabrieularyssa",
            "phone_number": "8499552200",
            "is_medic": True,
        }
        cls.user_data = {
            "username": "super",
            "password": "1234",
            "first_name": "gabriela",
            "last_name": "oliveira",
            "phone_number": 123456,
        }
        cls.user = Account.objects.create_superuser(**cls.user_data)

    def test_create_specialty_fail(self):
        """
        Verifica que não é livre a criação de uma especialidade
        """
        response = self.client.post(self.register_url, self.specialty_data)

        expected_status_code = status.HTTP_401_UNAUTHORIZED
        result_status_code = response.status_code

        self.assertEqual(expected_status_code, result_status_code)

    def test_create_specialty(self):
        """
        Verifica se o admin pode criar uma especialidade
        """
        token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION="Token " + token.key)
        res_admin = self.client.post(self.register_url, self.specialty_data)
        self.assertEqual(status.HTTP_201_CREATED, res_admin.status_code)
