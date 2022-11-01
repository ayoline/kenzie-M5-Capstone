from django.db import models


class Categorie(models.Model):
    id = models.IntegerField()
    color = models.CharField(max_length=20, unique=True)
    description = models.CharField(max_length=255)
