from django.db import models
from requestapp.manager import CategoryManager


class Category(models.Model):
    name = models.CharField(max_length=100)
    active = models.BooleanField(default=True)

    objects = CategoryManager()

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'requestapp'