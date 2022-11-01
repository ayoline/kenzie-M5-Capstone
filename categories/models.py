from django.db import models


class Category(models.Model):
    color = models.CharField(max_length=20, unique=True)
    description = models.CharField(max_length=255)
