from django.db import models


class Chart(models.Model):
    is_pregnant = models.BooleanField()
    is_diabetic = models.BooleanField()
    is_smoker = models.BooleanField()
    is_allergic = models.BooleanField()
    heart_disease = models.BooleanField()
    dificulty_healing = models.BooleanField()
    use_medication = models.BooleanField()
    other_information = models.TextField()
