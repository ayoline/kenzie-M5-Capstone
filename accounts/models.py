from django.db import models
from django.contrib.auth.models import AbstractUser


class Account(AbstractUser):
    first_name = models.CharField(max_length=255, blank=False)
    last_name = models.CharField(max_length=255, blank=False)
    phone_number = models.CharField(max_length=255, blank=False)
    is_medic = models.BooleanField(default=False, blank=False)

    REQUIRED_FIELDS = ["first_name", "last_name", "phone_number"]
