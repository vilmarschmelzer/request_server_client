from django.db import models
from .category import Category


class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category)
    active = models.BooleanField(default=True)

    class Meta:
        app_label = 'requestapp'