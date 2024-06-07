import re
from enum import Enum

from django.core.exceptions import ValidationError
from django.db import models

from network.models.vlan import VLAN
from network.models.wifi import WifiNetwork

class ConnectionType(Enum):
    ETHERNET = "ethernet"
    WIFI = "wifi"

    @classmethod
    def choices(cls) -> list[tuple[str, str]]:
        """Choices for the Connection Types"""
        return [(connection.name, connection.value.capitalize()) for connection in cls]


class Device(models.Model):
    name = models.CharField(max_length=100)
    mac_address = models.CharField(max_length=17, unique=True)
    ip_address = models.GenericIPAddressField(blank=True, null=True, unique=True)
    vlan = models.ForeignKey(VLAN, on_delete=models.CASCADE, blank=True, null=True)
    wifi = models.ForeignKey(WifiNetwork, on_delete=models.CASCADE, blank=True, null=True)
    connection_type = models.CharField(max_length=10, choices=ConnectionType.choices())

    def __str__(self):
        return self.name

    def clean(self):
        super().clean()

        if not self.mac_address_validation(self.mac_address):
            raise ValidationError("Invalid MAC Address format")

    @staticmethod
    def mac_address_validation(mac_address: str) -> bool:
        MAC_ADDRESS_PATTERN = r"^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})|([0-9a-fA-F]{4}\.[0-9a-fA-F]{4}\.[0-9a-fA-F]{4})$"
        return re.match(MAC_ADDRESS_PATTERN, mac_address) is not None

    class Meta:
        abstract = True


class ClientDevice(Device):
    pass


class NetworkDeviceType(Enum):
    ROUTER = "router"
    SWITCH = "switch"
    ACCESS_POINT = "access_point"

    @classmethod
    def choices(cls) -> list[tuple[str, str]]:
        """Choices for the Network Device Types"""
        return [(device.name, device.value.capitalize()) for device in cls]


class NetworkDevice(Device):
    device_type = models.CharField(max_length=20, choices=NetworkDeviceType.choices())
