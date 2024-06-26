from common.utils.config import get_config_value, update_config_value
from django.shortcuts import redirect, render
from django.urls import reverse


def index(request):
    if request.method == "POST":
        if "base_ip-submit" in request.POST:
            base_ip = request.POST.get("base_ip")
            update_config_value("base_ip", base_ip)
            return redirect(reverse("network_index"))
        elif "router_ip-submit" in request.POST:
            router_ip = request.POST.get("router_ip")
            update_config_value("router_ip", router_ip)
            return redirect(reverse("network_index"))

    base_ip = get_config_value("base_ip", "0.0")
    router_ip = get_config_value("router_ip", "0.0.0.0")

    return render(request, "network/index.html", {"base_ip": base_ip, "router_ip": router_ip})
