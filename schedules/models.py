from datetime import datetime
from django.db import models
from django.utils import timezone


class Schedule(models.Model):
    description = models.TextField()
    start_at = models.DateTimeField(default=timezone.now())
    completed = models.BooleanField(default=False)
    step = models.IntegerField(default=1)
    is_active = models.BooleanField(default=True)

    medic = models.ForeignKey(
        "medics.Medic",
        on_delete=models.CASCADE,
        related_name="schedules",
    )

    patient = models.ForeignKey(
        "patients.Patient",
        on_delete=models.CASCADE,
        related_name="schedules",
    )

    specialty = models.ForeignKey(
        "specialties.Specialty",
        on_delete=models.CASCADE,
        related_name="schedules",
    )
