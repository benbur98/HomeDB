# Generated by Django 5.0.2 on 2024-03-19 22:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="IpRange",
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
                ("start_address", models.GenericIPAddressField()),
                ("end_address", models.GenericIPAddressField()),
                ("num_addresses", models.PositiveIntegerField()),
                ("description", models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="VLAN",
            fields=[
                (
                    "vlan_id",
                    models.IntegerField(primary_key=True, serialize=False, unique=True),
                ),
                ("name", models.CharField(max_length=100)),
                ("description", models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="WifiNetwork",
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
                ("ssid", models.CharField(max_length=100)),
                ("password", models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="ClientDevice",
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
                ("name", models.CharField(max_length=100)),
                ("mac_address", models.CharField(max_length=17, unique=True)),
                (
                    "ip_address",
                    models.GenericIPAddressField(blank=True, null=True, unique=True),
                ),
                (
                    "connection_type",
                    models.CharField(
                        choices=[("ethernet", "Ethernet"), ("wifi", "WiFi")],
                        max_length=10,
                    ),
                ),
                (
                    "vlan",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="network.vlan"
                    ),
                ),
                (
                    "wifi",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="network.wifinetwork",
                    ),
                ),
            ],
        ),
    ]
