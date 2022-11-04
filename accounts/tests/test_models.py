from django.test import TestCase
from accounts.models import Account


class AccountModelClass(TestCase):
    @classmethod
    def setUpTestData(cls):

        cls.account_data = {
            "first_name": "Adriana",
            "last_name": "Silva",
            "username": "Drika",
            "phone_number": "21947852540",
            "is_medic": True,
        }
        cls.account = Account.objects.create(**cls.account_data)

    def test_account_fields(self):
        self.assertEqual(self.account.first_name, self.account_data["first_name"])
        self.assertEqual(self.account.last_name, self.account_data["last_name"])
        self.assertEqual(self.account.username, self.account_data["username"])
        self.assertEqual(self.account.phone_number, self.account_data["phone_number"])
        self.assertEqual(self.account.is_medic, self.account_data["is_medic"])
