# Generated by Django 4.1.2 on 2022-11-09 02:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("schedules", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="schedule",
            name="start_at",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2022, 11, 9, 2, 23, 41, 247311, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
