from django.db import models


class Medic(models.Model):
    crm = models.CharField(max_length=50, unique=True)

    address = models.ForeignKey(
        "addresses.Address",
        on_delete=models.CASCADE,
        related_name="medics",
    )

    category = models.ForeignKey(
        "categories.Category",
        on_delete=models.CASCADE,
        related_name="medics",
    )

    specialty = models.ForeignKey(
        "specialties.Specialty",
        on_delete=models.CASCADE,
        related_name="medics",
    )

    account = models.ForeignKey(
        "accounts.Account",
        on_delete=models.CASCADE,
        related_name="medics",
    )
