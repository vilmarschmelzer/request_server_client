from django.db import models


class Estado(models.Model):
    abbreviation = models.CharField(max_length=5, primary_key=True)
    name = models.CharField(max_length=200)

    class Meta:
        app_label = 'requestapp'