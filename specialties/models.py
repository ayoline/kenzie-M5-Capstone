from django.db import models


class Specialty(models.Model):
    name = models.CharField(max_length=150, unique=True)
