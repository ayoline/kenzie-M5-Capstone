from django.db import models


class Address(models.Model):
    street = models.CharField(max_length=255)
    number = models.IntegerField()
    cep = models.CharField(max_length=8)
    state = models.CharField(max_length=255)
    district = models.CharField(max_length=2)
