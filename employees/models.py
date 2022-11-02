from django.db import models


class employee(models.Model):
    cpf = models.CharField(max_length=14, unique=True)

    address = models.ForeignKey(
        "addresses.Address",
        on_delete=models.CASCADE,
        related_name="employees",
    )

    account = models.ForeignKey(
        "accounts.Account",
        on_delete=models.CASCADE,
        related_name="employees",
    )
