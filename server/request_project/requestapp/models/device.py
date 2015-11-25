from django.db import models


class Device(models.Model):
    imei = models.CharField(max_length=18, primary_key=True)
    last_request_id = models.IntegerField(default=0)
    active = models.BooleanField(default=True)

    class Meta:
        app_label = 'requestapp'