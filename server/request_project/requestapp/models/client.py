from django.db import models
from .address import Address


class Client(Address):
    document = models.CharField(max_length=14, primary_key=True)
    name = models.CharField(max_length=255)

    class Meta:
        app_label = 'requestapp'