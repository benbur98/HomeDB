from django.shortcuts import get_object_or_404, redirect, render

from ..forms import ClientDeviceForm, NetworkDeviceForm
from ..models import ClientDevice, NetworkDevice, VLAN, WifiNetwork

def index(request):
    client_devices = ClientDevice.objects.all()
    network_devices = NetworkDevice.objects.all()
    return render(request, "network/device/index.html", {"client_devices": client_devices, "network_devices": network_devices})


def create(request):
    vlan_options = [(vlan.vlan_id, str(vlan)) for vlan in VLAN.objects.all()]
    wifi_options = [(wifi.id, wifi.ssid) for wifi in WifiNetwork.objects.all()]

    if request.method == "POST":
        if "client" in request.POST:
            client_form = ClientDeviceForm(request.POST, vlan_options=vlan_options, wifi_options=wifi_options)
            if client_form.is_valid():
                client_form.save()
                return redirect("device.index")
        elif "network" in request.POST:
            network_form = NetworkDeviceForm(request.POST, vlan_options=vlan_options, wifi_options=wifi_options)
            if network_form.is_valid():
                network_form.save()
                return redirect("device.index")
    else:
        client_form = ClientDeviceForm(vlan_options=vlan_options, wifi_options=wifi_options)
        network_form = NetworkDeviceForm(vlan_options=vlan_options, wifi_options=wifi_options)

    if not client_form:
        client_form = ClientDeviceForm(vlan_options=vlan_options, wifi_options=wifi_options)
    if not network_form:
        network_form = NetworkDeviceForm(vlan_options=vlan_options, wifi_options=wifi_options)

    return render(request, "network/device/create.html", {"client_form": client_form, "network_form": network_form, "show_form": False})


def edit_client(request, id: int):
    device = get_object_or_404(ClientDevice, id=id)

    vlan_options = [(vlan.vlan_id, f"{vlan.vlan_id} - {vlan.name}") for vlan in VLAN.objects.all()]
    wifi_options = [(wifi.id, wifi.ssid) for wifi in WifiNetwork.objects.all()]

    if request.method == "POST":
        form = ClientDeviceForm(request.POST, instance=device, vlan_options=vlan_options, wifi_options=wifi_options)
        if form.is_valid():
            form.save()
            return redirect("device.index")
    else:
        form = ClientDeviceForm(instance=device, vlan_options=vlan_options, wifi_options=wifi_options)

    return render(request, "network/device/client_edit.html", {"form": form, "device": device})


def edit_network(request, id: int):
    device = get_object_or_404(NetworkDevice, id=id)

    vlan_options = [(vlan.vlan_id, f"{vlan.vlan_id} - {vlan.name}") for vlan in VLAN.objects.all()]
    wifi_options = [(wifi.id, wifi.ssid) for wifi in WifiNetwork.objects.all()]

    if request.method == "POST":
        form = NetworkDeviceForm(request.POST, instance=device, vlan_options=vlan_options, wifi_options=wifi_options)
        if form.is_valid():
            form.save()
            return redirect("device.index")
    else:
        form = NetworkDeviceForm(instance=device, vlan_options=vlan_options, wifi_options=wifi_options)

    return render(request, "network/device/network_edit.html", {"form": form, "device": device})


def delete_client(request, id: int):
    device = get_object_or_404(ClientDevice, id=id)
    device.delete()
    return redirect("device.index")


def delete_network(request, id: int):
    device = get_object_or_404(NetworkDevice, id=id)
    device.delete()
    return redirect("device.index")
