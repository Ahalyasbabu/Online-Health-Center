from django.db import models


# Create your models here.
class TimeSlots(models.Model):
    timeSlot= models.CharField(max_length=20)
    dateSlot= models.CharField(max_length=10)
    availability= models.CharField(max_length=10)
