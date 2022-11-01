from django.db import models


class Patient(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    cpf = models.CharField(max_length=14, unique=True)

    address = models.ForeignKey(
        "addresses.Address",
        on_delete=models.CASCADE,
        related_name="patients",
    )

    category = models.ForeignKey(
        "categories.Category",
        on_delete=models.CASCADE,
        related_name="patients",
    )

    chart = models.ForeignKey(
        "charts.Chart",
        on_delete=models.CASCADE,
        related_name="patients",
    )
