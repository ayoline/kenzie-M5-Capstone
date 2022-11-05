from django.db import models


class Employee(models.Model):
    cpf = models.CharField(max_length=14, unique=True)

    address = models.OneToOneField(
        "addresses.Address",
        on_delete=models.CASCADE,
        related_name="employees",
    )

    account = models.OneToOneField(
        "accounts.Account",
        on_delete=models.CASCADE,
        related_name="employees",
    )
