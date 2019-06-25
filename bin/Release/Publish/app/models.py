"""
Definition of models.
"""

from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Area(models.Model):
    name = models.CharField(max_length=120)
 
    def __str__(self):
        return self.name

class Feedback(models.Model):
    customer_first_name = models.CharField(max_length=120)
    customer_last_name = models.CharField(max_length=120)
    email = models.EmailField()
    area = models.ForeignKey(Area, on_delete=models.PROTECT)
    details = models.TextField()
    followup = models.BooleanField()
    date = models.DateField(auto_now_add=True)
 
    def __str__(self):
        return self.customer_first_name

class Location(models.Model):
    name = models.CharField(max_length=120)
    icon = models.CharField(max_length=120)
    long = models.FloatField()
    lat = models.FloatField()
 
    def __str__(self):
        return self.name

class Show(models.Model):
    showName = models.CharField(max_length=120)
    showLocation = models.CharField(max_length=120)
    showTime = models.TimeField()
    showMessage = models.CharField(max_length=120)
    showLong = models.FloatField(null=True)
    showLat = models.FloatField(null=True)
 
 
    def __str__(self):
        return self.showName


class PopupLocation(models.Model):
    name = models.CharField(max_length=120)
    message = models.CharField(max_length=120)
    long = models.FloatField()
    lat = models.FloatField()

    def __str__(self):
        return self.name




