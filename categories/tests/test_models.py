from django.test import TestCase
from categories.models import Category


class CategoryModelClass(TestCase):
    @classmethod
    def setUpTestData(cls):

        cls.category_data = {
            "color": "green",
            "description": "uma descrição",
        }
        cls.category = Category.objects.create(**cls.category_data)

    def test_category_fields(self):
        self.assertEqual(self.category.color, self.category_data["color"])
        self.assertEqual(self.category.description, self.category_data["description"])
