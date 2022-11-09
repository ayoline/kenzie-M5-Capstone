from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from accounts.models import Account
from medics.models import Medic
from addresses.models import Address
from categories.models import Category
from specialties.models import Specialty


class MedicsViewTest(APITestCase):
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

        cls.specialty_data_1 = {"name": "otorrino"}

        cls.specialty_data_2 = {"name": "otorrino2"}

        cls.medic_data_1 = {"crm": "12312312312"}

        cls.medic_user_data_1 = {
            "first_name": "anderson",
            "last_name": "alves",
            "phone_number": "12345565565",
            "username": "anderson",
            "password": "anderson",
        }

        cls.medic_data_2 = {"crm": "23232323232"}

        cls.medic_user_data_2 = {
            "first_name": "ferreira",
            "last_name": "alves",
            "phone_number": "77777777777",
            "username": "ferreira",
            "password": "ferreira",
        }

    def test_create_medic_using_user_admin(self):
        admin = Account.objects.create_superuser(**self.user_admin_data)
        token = Token.objects.create(user=admin)

        self.client.credentials(HTTP_AUTHORIZATION="Token " + token.key)

        category = Category.objects.create(**self.category_data_1)

        specialty = Specialty.objects.create(**self.specialty_data_1)

        response = self.client.post(
            "/api/medic/",
            {
                **self.medic_data_1,
                "address": self.address_data_1,
                "account": self.medic_user_data_1,
                "category_id": category.id,
                "specialty_id": specialty.id,
            },
            format="json",
        )

        self.assertEqual(response.status_code, 201)

        medic = Medic.objects.first()

        self.assertEqual(self.medic_data_1["crm"], medic.crm)

        self.assertEqual(self.address_data_1["street"], medic.address.street)
        self.assertEqual(self.address_data_1["number"], medic.address.number)
        self.assertEqual(self.address_data_1["cep"], medic.address.cep)
        self.assertEqual(self.address_data_1["state"], medic.address.state)
        self.assertEqual(self.address_data_1["district"], medic.address.district)

        self.assertEqual(self.medic_user_data_1["first_name"], medic.account.first_name)
        self.assertEqual(self.medic_user_data_1["last_name"], medic.account.last_name)
        self.assertEqual(
            self.medic_user_data_1["phone_number"], medic.account.phone_number
        )
        self.assertEqual(self.medic_user_data_1["username"], medic.account.username)
        self.assertEqual(False, medic.account.is_superuser)

        self.assertEqual(category.id, medic.category.id)

        self.assertEqual(specialty.id, medic.specialty.id)

    def test_create_medic_using_user_not_admin(self):
        admin = Account.objects.create_user(**self.user_admin_data)
        token = Token.objects.create(user=admin)

        self.client.credentials(HTTP_AUTHORIZATION="Token " + token.key)

        category = Category.objects.create(**self.category_data_1)

        specialty = Specialty.objects.create(**self.specialty_data_1)

        response = self.client.post(
            "/api/medic/",
            {
                **self.medic_data_1,
                "address": self.address_data_1,
                "account": self.medic_user_data_1,
                "category_id": category.id,
                "specialty_id": specialty.id,
            },
            format="json",
        )

        self.assertEqual(response.status_code, 403)

        responseJson = response.json()

        self.assertEqual(
            responseJson["detail"], "You do not have permission to perform this action."
        )

    def test_update_medic_using_user_admin(self):
        admin = Account.objects.create_superuser(**self.user_admin_data)
        token = Token.objects.create(user=admin)

        self.client.credentials(HTTP_AUTHORIZATION="Token " + token.key)

        category_1 = Category.objects.create(**self.category_data_1)

        specialty_1 = Specialty.objects.create(**self.specialty_data_1)

        category_2 = Category.objects.create(**self.category_data_2)

        specialty_2 = Specialty.objects.create(**self.specialty_data_2)

        address = Address.objects.create(**self.address_data_1)

        account = Account.objects.create_user(**self.medic_user_data_1)

        medic = Medic.objects.create(
            **self.medic_data_1,
            account=account,
            category=category_1,
            specialty=specialty_1,
            address=address,
        )

        response = self.client.patch(
            f"/api/medic/{medic.id}/",
            {
                **self.medic_data_2,
                "account": self.medic_user_data_2,
                "category_id": category_2.id,
                "specialty_id": specialty_2.id,
            },
            format="json",
        )

        self.assertEqual(response.status_code, 200)

        medic = Medic.objects.get(id=medic.id)

        self.assertEqual(self.medic_data_2["crm"], medic.crm)

        self.assertEqual(self.medic_user_data_2["first_name"], medic.account.first_name)
        self.assertEqual(self.medic_user_data_2["last_name"], medic.account.last_name)
        self.assertEqual(
            self.medic_user_data_2["phone_number"], medic.account.phone_number
        )
        self.assertEqual(self.medic_user_data_2["username"], medic.account.username)
        self.assertEqual(False, medic.account.is_superuser)

        self.assertEqual(category_2.id, medic.category.id)

        self.assertEqual(specialty_2.id, medic.specialty.id)

    def test_update_medic_using_other_user(self):
        other_user = Account.objects.create_user(**self.user_admin_data)
        token = Token.objects.create(user=other_user)

        self.client.credentials(HTTP_AUTHORIZATION="Token " + token.key)

        category_1 = Category.objects.create(**self.category_data_1)

        specialty_1 = Specialty.objects.create(**self.specialty_data_1)

        category_2 = Category.objects.create(**self.category_data_2)

        specialty_2 = Specialty.objects.create(**self.specialty_data_2)

        address = Address.objects.create(**self.address_data_1)

        account = Account.objects.create_user(**self.medic_user_data_1)

        medic = Medic.objects.create(
            **self.medic_data_1,
            account=account,
            category=category_1,
            specialty=specialty_1,
            address=address,
        )

        response = self.client.patch(
            f"/api/medic/{medic.id}/",
            {
                **self.medic_data_2,
                "account": self.medic_user_data_2,
                "category_id": category_2.id,
                "specialty_id": specialty_2.id,
            },
            format="json",
        )

        responseJson = response.json()

        self.assertEqual(response.status_code, 403)

        self.assertEqual(
            responseJson["detail"], "You do not have permission to perform this action."
        )

    def test_update_medic_using_owner_user(self):
        owner_user = Account.objects.create_user(**self.medic_user_data_1)
        token = Token.objects.create(user=owner_user)

        self.client.credentials(HTTP_AUTHORIZATION="Token " + token.key)

        category_1 = Category.objects.create(**self.category_data_1)

        specialty_1 = Specialty.objects.create(**self.specialty_data_1)

        category_2 = Category.objects.create(**self.category_data_2)

        specialty_2 = Specialty.objects.create(**self.specialty_data_2)

        address = Address.objects.create(**self.address_data_1)

        medic = Medic.objects.create(
            **self.medic_data_1,
            account=owner_user,
            category=category_1,
            specialty=specialty_1,
            address=address,
        )

        response = self.client.patch(
            f"/api/medic/{medic.id}/",
            {
                **self.medic_data_2,
                "account": self.medic_user_data_2,
                "category_id": category_2.id,
                "specialty_id": specialty_2.id,
            },
            format="json",
        )

        self.assertEqual(response.status_code, 200)

        medic = Medic.objects.first()

        self.assertEqual(self.medic_data_2["crm"], medic.crm)

        self.assertEqual(self.medic_user_data_2["first_name"], medic.account.first_name)
        self.assertEqual(self.medic_user_data_2["last_name"], medic.account.last_name)
        self.assertEqual(
            self.medic_user_data_2["phone_number"], medic.account.phone_number
        )
        self.assertEqual(self.medic_user_data_2["username"], medic.account.username)
        self.assertEqual(False, medic.account.is_superuser)

        self.assertEqual(category_2.id, medic.category.id)

        self.assertEqual(specialty_2.id, medic.specialty.id)

    def test_list_medics(self):

        category_1 = Category.objects.create(**self.category_data_1)

        specialty_1 = Specialty.objects.create(**self.specialty_data_1)

        category_2 = Category.objects.create(**self.category_data_2)

        specialty_2 = Specialty.objects.create(**self.specialty_data_2)

        address_1 = Address.objects.create(**self.address_data_1)

        address_2 = Address.objects.create(**self.address_data_2)

        account_1 = Account.objects.create_user(**self.medic_user_data_1)

        account_2 = Account.objects.create_user(**self.medic_user_data_2)

        Medic.objects.create(
            **self.medic_data_1,
            account=account_1,
            category=category_1,
            specialty=specialty_1,
            address=address_1,
        )

        Medic.objects.create(
            **self.medic_data_2,
            account=account_2,
            category=category_2,
            specialty=specialty_2,
            address=address_2,
        )

        response = self.client.get("/api/medic/")

        self.assertEqual(response.status_code, 200)

        responseJson = response.json()

        self.assertEqual(len(responseJson), 2)

    def test_getone_medics_using_user_admin(self):
        admin = Account.objects.create_superuser(**self.user_admin_data)
        token = Token.objects.create(user=admin)

        self.client.credentials(HTTP_AUTHORIZATION="Token " + token.key)

        category = Category.objects.create(**self.category_data_1)

        specialty = Specialty.objects.create(**self.specialty_data_1)

        address = Address.objects.create(**self.address_data_1)

        account = Account.objects.create_user(**self.medic_user_data_1)

        medic = Medic.objects.create(
            **self.medic_data_1,
            account=account,
            category=category,
            specialty=specialty,
            address=address,
        )

        response = self.client.get(f"/api/medic/{medic.id}/")

        self.assertEqual(response.status_code, 200)

        responseJson = response.json()

        self.assertEqual(self.medic_data_1["crm"], responseJson["crm"])

        self.assertEqual(self.address_data_1["street"], responseJson["address"]["street"])
        self.assertEqual(self.address_data_1["number"], responseJson["address"]["number"])
        self.assertEqual(self.address_data_1["cep"], responseJson["address"]["cep"])
        self.assertEqual(self.address_data_1["state"], responseJson["address"]["state"])
        self.assertEqual(
            self.address_data_1["district"], responseJson["address"]["district"]
        )

        self.assertEqual(
            self.medic_user_data_1["first_name"], responseJson["account"]["first_name"]
        )
        self.assertEqual(
            self.medic_user_data_1["last_name"], responseJson["account"]["last_name"]
        )
        self.assertEqual(
            self.medic_user_data_1["phone_number"],
            responseJson["account"]["phone_number"],
        )
        self.assertEqual(
            self.medic_user_data_1["username"], responseJson["account"]["username"]
        )

    def test_getone_medics_using_other_user(self):
        other_user = Account.objects.create_user(**self.medic_user_data_2)
        token = Token.objects.create(user=other_user)

        self.client.credentials(HTTP_AUTHORIZATION="Token " + token.key)

        category = Category.objects.create(**self.category_data_1)

        specialty = Specialty.objects.create(**self.specialty_data_1)

        address = Address.objects.create(**self.address_data_1)

        account = Account.objects.create_user(**self.medic_user_data_1)

        medic = Medic.objects.create(
            **self.medic_data_1,
            account=account,
            category=category,
            specialty=specialty,
            address=address,
        )

        response = self.client.get(f"/api/medic/{medic.id}/")

        self.assertEqual(response.status_code, 403)

        responseJson = response.json()

        self.assertEqual(
            responseJson["detail"], "You do not have permission to perform this action."
        )

    def test_getone_medics_using_owner_user(self):
        user_owner = Account.objects.create_user(**self.medic_user_data_1)
        token = Token.objects.create(user=user_owner)

        self.client.credentials(HTTP_AUTHORIZATION="Token " + token.key)

        category = Category.objects.create(**self.category_data_1)

        specialty = Specialty.objects.create(**self.specialty_data_1)

        address = Address.objects.create(**self.address_data_1)

        medic = Medic.objects.create(
            **self.medic_data_1,
            account=user_owner,
            category=category,
            specialty=specialty,
            address=address,
        )

        response = self.client.get(f"/api/medic/{medic.id}/")

        self.assertEqual(response.status_code, 200)

        responseJson = response.json()

        self.assertEqual(self.medic_data_1["crm"], responseJson["crm"])

        self.assertEqual(self.address_data_1["street"], responseJson["address"]["street"])
        self.assertEqual(self.address_data_1["number"], responseJson["address"]["number"])
        self.assertEqual(self.address_data_1["cep"], responseJson["address"]["cep"])
        self.assertEqual(self.address_data_1["state"], responseJson["address"]["state"])
        self.assertEqual(
            self.address_data_1["district"], responseJson["address"]["district"]
        )

        self.assertEqual(
            self.medic_user_data_1["first_name"], responseJson["account"]["first_name"]
        )
        self.assertEqual(
            self.medic_user_data_1["last_name"], responseJson["account"]["last_name"]
        )
        self.assertEqual(
            self.medic_user_data_1["phone_number"],
            responseJson["account"]["phone_number"],
        )
        self.assertEqual(
            self.medic_user_data_1["username"], responseJson["account"]["username"]
        )

    def test_delete_medics_using_user_admin(self):
        admin = Account.objects.create_superuser(**self.user_admin_data)
        token = Token.objects.create(user=admin)

        self.client.credentials(HTTP_AUTHORIZATION="Token " + token.key)

        category = Category.objects.create(**self.category_data_1)

        specialty = Specialty.objects.create(**self.specialty_data_1)

        address = Address.objects.create(**self.address_data_1)

        account = Account.objects.create_user(**self.medic_user_data_1)

        medic = Medic.objects.create(
            **self.medic_data_1,
            account=account,
            category=category,
            specialty=specialty,
            address=address,
        )

        response = self.client.delete(f"/api/medic/{medic.id}/")

        self.assertEqual(response.status_code, 204)

        self.assertEqual(len(Medic.objects.all()), 0)

    def test_delete_medics_using_user_admin(self):
        other_user = Account.objects.create_user(**self.user_admin_data)
        token = Token.objects.create(user=other_user)

        self.client.credentials(HTTP_AUTHORIZATION="Token " + token.key)

        category = Category.objects.create(**self.category_data_1)

        specialty = Specialty.objects.create(**self.specialty_data_1)

        address = Address.objects.create(**self.address_data_1)

        account = Account.objects.create_user(**self.medic_user_data_1)

        medic = Medic.objects.create(
            **self.medic_data_1,
            account=account,
            category=category,
            specialty=specialty,
            address=address,
        )

        response = self.client.delete(f"/api/medic/{medic.id}/")

        self.assertEqual(response.status_code, 403)

        responseJson = response.json()

        self.assertEqual(
            responseJson["detail"], "You do not have permission to perform this action."
        )
