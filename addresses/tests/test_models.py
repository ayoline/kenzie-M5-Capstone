from django.test import TestCase
from addresses.models import Address


class AddressModelClass(TestCase):
    @classmethod
    def setUpTestData(cls):

        cls.address_data = {
            "street": "Rua Oliveira",
            "number": 35,
            "cep": "24890587",
            "state": "MG",
            "district": "Bandeirantes",
        }
        cls.address = Address.objects.create(**cls.address_data)

    def test_address_fields(self):
        self.assertEqual(self.address.street, self.address_data["street"])
        self.assertEqual(self.address.number, self.address_data["number"])
        self.assertEqual(self.address.cep, self.address_data["cep"])
        self.assertEqual(self.address.state, self.address_data["state"])
        self.assertEqual(self.address.district, self.address_data["district"])
