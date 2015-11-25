from django.db import models
from .address import Address
from .device import Device
from .client import Client


class Request(Address):
    device = models.ForeignKey(Device, null=True)
    device_request_id = models.IntegerField(null=True)

    date = models.DateTimeField(auto_now_add=True)
    client = models.ForeignKey(Client)
    observation = models.TextField(null=True)

    class Meta:
        app_label = 'requestapp'