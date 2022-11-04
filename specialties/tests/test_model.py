from django.test import TestCase
from specialties.models import Specialty


class SpecialtiesModelTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        # cria em forma de dict
        cls.specialty_data = {
            "name": "otorrino",
        }

        # cria um obj
        cls.specialty = Specialty.objects.create(**cls.specialty_data)

    def test_name_max_length(self):
        """
        Verifica a propriedade de tamanho máximo de `name`
        """
        expected_max_length = 150
        result_max_length = Specialty._meta.get_field("name").max_length
        msg = f"Verifique se a propriedade `max_length` de name foi definida como {expected_max_length}"

        self.assertEqual(expected_max_length, result_max_length, msg)

    def test_specialty(self):
        """
        Verifica se o banco esta persistindo o que deve persistir
        """
        expected_attribute = self.specialty.name
        result_attribute = self.specialty_data["name"]
        self.assertEqual(expected_attribute, result_attribute)
