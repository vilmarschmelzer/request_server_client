from django.db import models
from .city import City


class District(models.Model):
    name = models.CharField(max_length=255)
    city = models.ForeignKey(City)

    class Meta:
        app_label = 'requestapp'