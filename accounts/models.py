from django.db import models
from django.contrib.auth.models import AbstractUser


class Account(AbstractUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=20, unique=True)
    phone_number = models.CharField(max_length=50)
    is_medic = models.BooleanField(default=False)

    REQUIRED_FIELDS = ["first_name", "last_name", "phone_number"]
