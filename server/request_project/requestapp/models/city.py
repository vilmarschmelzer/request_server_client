from django.db import models
from .estado import Estado


class City(models.Model):
    name = models.CharField(max_length=255)
    estado = models.ForeignKey(Estado)

    class Meta:
        app_label = 'requestapp'