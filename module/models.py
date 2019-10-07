from django.db import models
from django.conf import settings
from django.utils import timezone

class Sensor(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    name = models.CharField(max_length=120)
    address = models.SlugField(unique=True)
    about = models.TextField()
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.name

class Sensor_data(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    value = models.SlugField(unique=True)
    date = models.DateTimeField(auto_now=True, auto_now_add=False)
    time = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.value
