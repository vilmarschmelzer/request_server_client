from django.db import models
from requestapp.manager import CategoryManager


class Category(models.Model):
    name = models.CharField(max_length=100)
    active = models.BooleanField(default=True)

    objects = CategoryManager()

    class Meta:
        app_label = 'requestapp'