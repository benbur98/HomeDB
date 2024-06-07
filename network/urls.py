from django.urls import include, path

from . import views

urlpatterns = [
    path("", views.index.index, name="network_index"),
    path(
        "vlan/",
        include(
            [
                path("", views.vlan.index, name="vlan.index"),
                path("create", views.vlan.create, name="vlan.create"),
                path("<int:vlan_id>/edit", views.vlan.edit, name="vlan.edit"),
                path("<int:vlan_id>/delete", views.vlan.delete, name="vlan.delete"),
            ]
        ),
    ),
    path(
        "wifi/",
        include(
            [
                path("", views.wifi.index, name="wifi.index"),
                path("create", views.wifi.create, name="wifi.create"),
                path("<int:id>/edit", views.wifi.edit, name="wifi.edit"),
                path("<int:id>/delete", views.wifi.delete, name="wifi.delete"),
            ]
        ),
    ),
    path(
        "device/",
        include(
            [
                path("", views.device.index, name="device.index"),
                path("create", views.device.create, name="device.create"),
                path(
                    "client/",
                    include(
                        [
                            path("<int:id>/edit", views.device.edit_client, name="client_device.edit"),
                            path("<int:id>/delete", views.device.delete_client, name="client_device.delete"),
                        ]
                    ),
                ),
                path(
                    "network/",
                    include(
                        [
                            path("<int:id>/edit", views.device.edit_network, name="network_device.edit"),
                            path("<int:id>/delete", views.device.delete_network, name="network_device.delete"),
                        ]
                    ),
                ),
            ]
        ),
    ),
    path(
        "rack/",
        include(
            [
                path("", views.rack.index, name="rack.index"),
                path("create", views.rack.create_rack, name="rack.create"),
                path("<int:id>/edit", views.rack.edit_rack, name="rack.edit"),
                path("<int:id>/delete", views.rack.delete_rack, name="rack.delete"),
                path("<int:rack_id>/items", views.rack.rack_index, name="rack_item.index"),
            ]
        ),
    ),
    path(
        "rack-item/",
        include(
            [
                path("create", views.rack.create_rack_item, name="rack_item.create"),
                path("<int:id>/edit", views.rack.edit_rack_item, name="rack_item.edit"),
                path("<int:id>/delete", views.rack.delete_rack_item, name="rack_item.delete"),
            ]
        ),
    ),
]
