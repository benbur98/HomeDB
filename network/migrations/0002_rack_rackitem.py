# Generated by Django 5.0.2 on 2024-06-06 18:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("network", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Rack",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                (
                    "width",
                    models.PositiveIntegerField(
                        choices=[(10, "WIDTH_10"), (19, "WIDTH_19"), (23, "WIDTH_23")]
                    ),
                ),
                ("rack_units", models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name="RackItem",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                ("rack_units", models.FloatField()),
                (
                    "rack",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="rack_items",
                        to="network.rack",
                    ),
                ),
            ],
        ),
    ]