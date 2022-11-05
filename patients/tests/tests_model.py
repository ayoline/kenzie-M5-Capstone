from django.test import TestCase
from patients.models import Patient
from categories.models import Category
from addresses.models import Address
from charts.models import Chart
from django.db import IntegrityError


class PatientsModelTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.patient_data = {
            "first_name": "Adriana",
            "last_name": "Silva",
            "cpf": "13678958236",
            "address_id": 2,
            "category_id": 2,
            "chart_id": 2,
        }
        cls.patient = Patient.objects.create(**cls.patient_data)

        cls.address_data = {
            "street": "Rua ValVerde",
            "number": 30,
            "cep": "14726826",
            "state": "MG",
            "district": "Centro",
            "city": "Belo Horizonte",
        }
        cls.address = Address.objects.create(**cls.address_data)

        cls.category_data = {
            "color": "verde",
            "description": "atende pela tarde",
        }
        cls.category = Category.objects.create(**cls.category_data)

        cls.chart_data = {
            "is_pregnant": False,
            "is_diabetic": True,
            "is_smoker": True,
            "is_allergic": True,
            "heart_disease": False,
            "dificulty_healing": False,
            "use_medication": True,
            "other_information": "Se encontra bem nervoso",
        }
        cls.chart = Chart.objects.create(**cls.chart_data)

        cls.patient_data = {
            "first_name": "Adriana",
            "last_name": "Silva",
            "cpf": "13678958236",
        }
        cls.patient = Patient.objects.create(**cls.patient_data,
                                             chart=cls.chart,
                                             address=cls.address,
                                             category=cls.category)

    def test_patient_fields(self):
        self.assertEqual(self.patient.first_name,
                         self.patient_data["first_name"])
        self.assertEqual(self.patient.last_name,
                         self.patient_data["last_name"])

    def test_patient_fields(self):
        self.assertEqual(self.patient.first_name, self.patient_data["first_name"])
        self.assertEqual(self.patient.last_name, self.patient_data["last_name"])
        self.assertEqual(self.patient.cpf, self.patient_data["cpf"])

    def test_patient_and_first_name(self):
        """
        Conferir informações entre patient e first_name
        """
        expected_first_name = "Adriana"
        result_first_name = self.patient.first_name
        msg = f"Verifique se o valor de `first_name` foi definida como {expected_first_name}"

        self.assertEqual(expected_first_name, result_first_name, msg)

    def test_cpf_max_length(self):
        """
        Verifica a propriedade de tamanho máximo de `cpf`
        """
        expected_max_length = 14
        result_max_length = Patient._meta.get_field("cpf").max_length
        msg = f"Verifique se a propriedade `max_length` de name foi definida como {expected_max_length}"

        self.assertEqual(expected_max_length, result_max_length, msg)


class PatientRelationshipTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.address_data = {
            "street": "Rua ValVerde",
            "number": 30,
            "cep": "14726826",
            "state": "MG",
            "district": "Centro",
            "city": "Belo Horizonte",
        }

        cls.category_data = {
            "color": "verde",
            "description": "atende pela tarde",
        }

        cls.chart_data = {
            "is_pregnant": False,
            "is_diabetic": True,
            "is_smoker": True,
            "is_allergic": True,
            "heart_disease": False,
            "dificulty_healing": False,
            "use_medication": True,
            "other_information": "Se encontra bem nervoso",
        }

        cls.patient_data = {
            "first_name": "Adriana",
            "last_name": "Silva",
            "cpf": "13678958236",
            "address_id": 1,
            "category_id": 1,
            "chart_id": 1,
        }

        cls.chart = Chart.objects.create(**cls.chart_data)
        cls.address = Address.objects.create(**cls.address_data)
        cls.category = Category.objects.create(**cls.category_data)
        cls.patient = Patient.objects.create(
            **cls.patient_data,
            chart=cls.chart,
            address=cls.address,
            category=cls.category,
        )

    def test_if_patient_can_have_an_address(self):
        """
        Verifica se um patient pode registrar um address relacionado
        """

        self.assertIs(self.address.patients, self.patient)

        self.assertIs(self.address, self.patient.address)

    def test_if_patient_can_have_a_chart(self):
        # Verifica se um paciente pode ter um chart relacionado

        self.assertIs(self.chart.patients, self.patient)

        self.assertIs(self.chart, self.patient.chart)

    def test_if_raise_error_when_patient_already_have_a_chart(self):
        """ Verifica se um erro é levantado ao atribuir o mesmo address a 
        outro patient """

        with self.assertRaises(IntegrityError):
            chart_two_data = {
                "is_pregnant": False,
                "is_diabetic": True,
                "is_smoker": True,
                "is_allergic": True,
                "heart_disease": False,
                "dificulty_healing": False,
                "use_medication": True,
                "other_information": "Se encontra bem nervoso",
            }

            patient_two_data = {
                "first_name": "Maria",
                "last_name": "Silva",
                "cpf": "13678958235",
            }

            chart_two = Chart.objects.create(**chart_two_data)
            patient_two = Patient.objects.create(**patient_two_data,
                                                 chart=chart_two,
                                                 address=self.address,
                                                 category=self.category,
                                                 )

    def test_if_raise_error_when_patient_already_have_a_chart(self):
        """ Verifica se um erro é levantado ao atribuir o mesmo chart a 
        outro patient """

        with self.assertRaises(IntegrityError):
            address_two_data = {
                "street": "rua das margaridas",
                "number": 30,
                "cep": "12345656",
                "state": "SP",
                "district": "bairro lalala",
                "city": "São Paulo",
            }

            patient_two_data = {
                "first_name": "Mari",
                "last_name": "Silva",
                "cpf": "13678958245",
            }

            address_two = Address.objects.create(**address_two_data)

            patient_two = Patient.objects.create(
                **patient_two_data,
                chart=self.chart,
                address=address_two,
                category=self.category,
            )

    def test_category_may_contain_multiple_patients(self):
        # Verifica se uma category pode ter vários pacientes relacionados
        patient_three_data = {
            "first_name": "Mari",
            "last_name": "Silva",
            "cpf": "13678958244",
        }
        patient_four_data = {
            "first_name": "Mari",
            "last_name": "Silva",
            "cpf": "13678958243",
        }

        address_three_data = {
            "street": "rua das margaridas",
            "number": 60,
            "cep": "12345652",
            "state": "SP",
            "district": "bairro lalala",
            "city": "São Paulo",
        }

        address_four_data = {
            "street": "rua das margaridas",
            "number": 50,
            "cep": "12345616",
            "state": "RJ",
            "district": "bairro lalala",
            "city": "São Paulo",
        }

        chart_three_data = {
            "is_pregnant": False,
            "is_diabetic": False,
            "is_smoker": True,
            "is_allergic": True,
            "heart_disease": False,
            "dificulty_healing": False,
            "use_medication": True,
            "other_information": "Se encontra bem nervoso",
        }

        chart_four_data = {
            "is_pregnant": False,
            "is_diabetic": False,
            "is_smoker": True,
            "is_allergic": False,
            "heart_disease": False,
            "dificulty_healing": False,
            "use_medication": True,
            "other_information": "Se encontra bem nervoso",
        }

        chart_three = Chart.objects.create(**chart_three_data)
        chart_four = Chart.objects.create(**chart_four_data)
        address_three = Address.objects.create(**address_three_data)
        address_four = Address.objects.create(**address_four_data)
        patient_three = Patient.objects.create(
            **patient_three_data,
            chart=chart_three,
            address=address_three,
            category=self.category,
        )

        patient_four = Patient.objects.create(
            **patient_four_data,
            chart=chart_four,
            address=address_four,
            category=self.category,
        )

        patients = []
        patients.append(self.patient)
        patients.append(patient_three)
        patients.append(patient_four)

        for patient in patients:
            self.assertIs(patient.category, self.category)
            self.assertEquals(len(patients), self.category.patients.count())

    def test__patient_cannot_belong_to_more_than_one_category(self):
        # Verifica se um paciente pode ter somente uma categoria relacionada
        patient_three_data = {
            "first_name": "Mari",
            "last_name": "Silva",
            "cpf": "13678958284",
        }
        patient_four_data = {
            "first_name": "Mari",
            "last_name": "Silva",
            "cpf": "13628958243",
        }

        address_three_data = {
            "street": "rua das margaridas",
            "number": 10,
            "cep": "12345602",
            "state": "SP",
            "district": "bairro lalala",
            "city": "São Paulo",
        }

        address_four_data = {
            "street": "rua das margaridas",
            "number": 70,
            "cep": "12325616",
            "state": "RJ",
            "district": "bairro lalala",
            "city": "São Paulo",
        }

        chart_three_data = {
            "is_pregnant": False,
            "is_diabetic": False,
            "is_smoker": True,
            "is_allergic": True,
            "heart_disease": False,
            "dificulty_healing": False,
            "use_medication": True,
            "other_information": "Se encontra bem nervoso",
        }

        chart_four_data = {
            "is_pregnant": False,
            "is_diabetic": False,
            "is_smoker": True,
            "is_allergic": False,
            "heart_disease": False,
            "dificulty_healing": False,
            "use_medication": True,
            "other_information": "Se encontra bem nervoso",
        }

        category_three_data = {
            "color": "blue",
            "description": "atende pela tarde",
        }

        category_three = Category.objects.create(**category_three_data)
        chart_three = Chart.objects.create(**chart_three_data)
        chart_four = Chart.objects.create(**chart_four_data)
        address_three = Address.objects.create(**address_three_data)
        address_four = Address.objects.create(**address_four_data)

        patient_three = Patient.objects.create(
            **patient_three_data,
            chart=chart_three,
            address=address_three,
            category=self.category,
        )

        patient_four = Patient.objects.create(
            **patient_four_data,
            chart=chart_four,
            address=address_four,
            category=self.category,
        )
        patients = []
        patients.append(patient_three)
        patients.append(patient_four)

        for patient in patients:
            patient.category = category_three
            patient.save()

        for patient in patients:
            self.assertNotIn(patient, self.category.patients.all())
            self.assertIn(patient, category_three.patients.all())
