from django.db import models
from .request import Request
from .item import Item


class RequestItem(models.Model):
    request = models.ForeignKey(Request)
    item = models.ForeignKey(Item)
    name = models.CharField(max_length=100)
    description = models.TextField(null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade = models.PositiveIntegerField(default={'min_value': 1, 'max_value':10})

    class Meta:
        app_label = 'requestapp'