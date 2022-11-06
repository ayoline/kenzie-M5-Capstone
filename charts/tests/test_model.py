from django.test import TestCase
from charts.models import Chart


class ChartModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.chart_data = {
            "is_pregnant": True,
            "is_diabetic": True,
            "is_smoker": True,
            "is_allergic": True,
            "heart_disease": False,
            "dificulty_healing": False,
            "use_medication": True,
            "other_information": "Apenas um teste de model a nivel de atributos",
        }
        cls.chart = Chart.objects.create(**cls.chart_data)

    def test_chart(self):
        """
        Verifica se o banco esta persistindo o que deve persistir
        """
        self.assertEqual(self.chart.is_pregnant, self.chart_data["is_pregnant"])
        self.assertEqual(self.chart.is_diabetic, self.chart_data["is_diabetic"])
        self.assertEqual(self.chart.is_smoker, self.chart_data["is_smoker"])
        self.assertEqual(self.chart.is_allergic, self.chart_data["is_allergic"])
        self.assertEqual(self.chart.heart_disease, self.chart_data["heart_disease"])
        self.assertEqual(
            self.chart.dificulty_healing, self.chart_data["dificulty_healing"]
        )
        self.assertEqual(
            self.chart.dificulty_healing, self.chart_data["dificulty_healing"]
        )
        self.assertEqual(self.chart.use_medication, self.chart_data["use_medication"])
        self.assertEqual(
            self.chart.other_information, self.chart_data["other_information"]
        )
