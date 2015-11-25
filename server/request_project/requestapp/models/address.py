from django.db import models
from .district import District


class Address(models.Model):
    address = models.CharField(max_length=255)
    address_number = models.CharField(max_length=30)
    district = models.ForeignKey(District)
    reference = models.TextField(null=True)

    class Meta:
        abstract = True
