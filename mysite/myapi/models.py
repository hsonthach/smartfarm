from django.db import models

# Create your models here.


class Device(models.Model):
    device_type = models.CharField(max_length=100)
    value = models.CharField(max_length=100)
    key = models.CharField(max_length=100)

    def __str__(self):
        return str(self.key) + '__' + str(self.value)
