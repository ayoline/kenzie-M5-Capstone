# Generated by Django 4.1.3 on 2022-11-07 02:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("schedules", "0002_alter_schedule_start_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="schedule",
            name="start_at",
            field=models.DateTimeField(
                default=datetime.datetime(2022, 11, 6, 23, 4, 54, 644607)
            ),
        ),
    ]
