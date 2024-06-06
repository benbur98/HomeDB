# Generated by Django 5.0.2 on 2024-06-06 18:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("network", "0003_alter_clientdevice_connection_type_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="rackitem",
            name="device",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="rack_item",
                to="network.networkdevice",
            ),
        ),
    ]
