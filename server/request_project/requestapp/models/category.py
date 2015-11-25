from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    active = models.BooleanField(default=True)

    class Meta:
        app_label = 'requestapp'