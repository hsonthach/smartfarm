from django.db import models

# Create your models here.


class Device(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    data = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    unit = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return str(self.id) + '__' + str(self.name) + '__' + str(self.data)
