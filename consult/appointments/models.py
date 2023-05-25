from django.db import models

# Create your models here.
class AppointmentsModel(models.Model):
    timeSlot= models.CharField(max_length=25)
    dateSlot= models.CharField(max_length=25)
    userId  = models.CharField(max_length=25)
    doctorId = models.CharField(max_length=25)
    status  = models.CharField(max_length=25)
    doctorName = models.CharField(max_length=25, default="default")
    patientName = models.CharField(max_length=25, default="default")


