# Generated by Django 4.1.2 on 2022-11-03 23:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("addresses", "0002_alter_address_district_alter_address_state"),
        ("charts", "0001_initial"),
        ("patients", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="patient",
            name="address",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="patients",
                to="addresses.address",
            ),
        ),
        migrations.AlterField(
            model_name="patient",
            name="chart",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="patients",
                to="charts.chart",
            ),
        ),
    ]