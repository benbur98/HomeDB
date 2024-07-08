# Generated by Django 5.0.2 on 2024-07-08 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("network", "0004_rackitem_device"),
    ]

    operations = [
        migrations.CreateModel(
            name="InfrastructureDevice",
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
                (
                    "device_type",
                    models.CharField(
                        choices=[
                            ("POWER", "Power"),
                            ("PATCH_PANEL", "Patch_panel"),
                            ("BLANK", "Blank"),
                            ("CABLE_MANAGEMENT", "Cable_management"),
                        ],
                        max_length=20,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.AlterField(
            model_name="networkdevice",
            name="device_type",
            field=models.CharField(
                choices=[
                    ("ROUTER", "Router"),
                    ("FIREWALL", "Firewall"),
                    ("SWITCH", "Switch"),
                    ("ACCESS_POINT", "Access_point"),
                    ("STORAGE", "Storage"),
                ],
                max_length=20,
            ),
        ),
    ]
