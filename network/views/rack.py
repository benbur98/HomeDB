from django.shortcuts import get_object_or_404, redirect, render

from ..forms import RackForm, RackItemForm
from ..models import NetworkDevice, Rack, RackItem

def index(request):
    racks = Rack.objects.all()
    return render(request, "network/rack/index.html", {"racks": racks})


def rack_index(request, rack_id):
    rack = get_object_or_404(Rack, id=rack_id)
    rack_items = RackItem.objects.filter(rack=rack)
    return render(request, "network/rack_item/index.html", {"rack": rack, "rack_items": rack_items})


def create_rack(request):
    if request.method == "POST":
        form = RackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("rack.index")
    else:
        form = RackForm()

    return render(request, "network/rack/create.html", {"form": form})


def create_rack_item(request):
    rack_options = [(rack.id, rack.name) for rack in Rack.objects.all()]
    device_options = [(device.id, device.name) for device in NetworkDevice.objects.all()]

    if request.method == "POST":
        form = RackItemForm(request.POST, rack_options=rack_options, device_options=device_options)
        if form.is_valid():
            form.save()
            return redirect("rack_item.index")
    else:
        form = RackItemForm(rack_options=rack_options, device_options=device_options)

    return render(request, "network/rack_item/create.html", {"form": form})


def edit_rack(request, rack_id: int):
    rack = get_object_or_404(Rack, rack_id=rack_id)

    if request.method == "POST":
        form = RackForm(request.POST, instance=rack)
        if form.is_valid():
            form.save()
            return redirect("rack.index")
    else:
        form = RackForm(instance=rack)

    return render(request, "network/rack/edit.html", {"form": form, "rack": rack})


def edit_rack_item(request, rack_item_id: int):
    rack_options = [(rack.id, rack.name) for rack in Rack.objects.all()]
    device_options = [(device.id, device.name) for device in NetworkDevice.objects.all()]

    rack_item = get_object_or_404(RackItem, rack_item_id=rack_item_id)

    if request.method == "POST":
        form = RackItemForm(request.POST, instance=rack_item, rack_options=rack_options, device_options=device_options)
        if form.is_valid():
            form.save()
            return redirect("rack_item.index")
    else:
        form = RackItemForm(instance=rack_item, rack_options=rack_options, device_options=device_options)

    return render(request, "network/rack_item/edit.html", {"form": form, "rack_item": rack_item})


def delete_rack(request, id: int):
    rack = get_object_or_404(Rack, id=id)
    rack.delete()
    return redirect("rack.index")


def delete_rack_item(request, id: int):
    rack_item = get_object_or_404(RackItem, id=id)
    rack_item.delete()
    return redirect("rack_item.index")
