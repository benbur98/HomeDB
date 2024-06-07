from django import forms

from .models import ClientDevice, NetworkDevice, Rack, RackItem, VLAN, WifiNetwork
from .models.device import ConnectionType, Device
from .models.ip import IpRange

class IpRangeForm(forms.Form):

    description = forms.CharField(widget=forms.Textarea(attrs={"style": "height:50px;"}), required=False)

    class Meta:
        model = IpRange
        fields = ["start_address", "end_address", "num_addresses", "description"]


class VLANForm(forms.ModelForm):

    description = forms.CharField(widget=forms.Textarea(attrs={"style": "height:50px;"}), required=False)

    class Meta:
        model = VLAN
        fields = ["vlan_id", "name", "description"]


class WifiForm(forms.ModelForm):
    class Meta:
        model = WifiNetwork
        fields = ["ssid", "password"]


class DeviceForm(forms.ModelForm):

    connection_type = forms.ChoiceField(
        choices=ConnectionType.choices(),
        widget=forms.Select(attrs={"class": "form-control"}),
    )

    class Meta:
        model = Device
        abstract = True
        fields = [
            "name",
            "mac_address",
            "vlan",
            "ip_address",
            "connection_type",
            "wifi",
        ]

    def __init__(self, *args, vlan_options=None, wifi_options=None, **kwargs):
        super(DeviceForm, self).__init__(*args, **kwargs)

        self.fields["vlan"].widget = forms.Select(choices=vlan_options, attrs={"class": "form-control"})

        empty_choice = [("", "None")]

        self.fields["wifi"].widget = forms.Select(choices=empty_choice + wifi_options, attrs={"class": "form-control"})
        self.fields["wifi"].required = False

    def clean(self):
        cleaned_data = super().clean()

        connection_type = cleaned_data.get("connection_type")
        wifi = cleaned_data.get("wifi")
        if connection_type == "ethernet" and wifi:
            raise forms.ValidationError("WiFi must be null for Ethernet Connections", code="invalid")
        if connection_type == "wifi" and not wifi:
            raise forms.ValidationError("WiFi must be set for WiFi Connections", code="invalid")

        return cleaned_data


class ClientDeviceForm(DeviceForm):
    class Meta(DeviceForm.Meta):
        model = ClientDevice


class NetworkDeviceForm(DeviceForm):
    class Meta(DeviceForm.Meta):
        model = NetworkDevice
        fields = DeviceForm.Meta.fields + ["device_type"]


class RackForm(forms.ModelForm):

    class Meta:
        model = Rack
        fields = ["name", "width", "rack_units"]


class RackItemForm(forms.ModelForm):

    class Meta:
        model = RackItem
        fields = ["name", "rack_units", "rack", "device"]

    def __init__(self, *args, rack_options=None, device_options=None, **kwargs):
        super(RackItemForm, self).__init__(*args, **kwargs)

        self.fields["rack"].widget = forms.Select(choices=rack_options, attrs={"class": "form-control"})

        self.fields["device"].widget = forms.Select(choices=device_options, attrs={"class": "form-control"})
