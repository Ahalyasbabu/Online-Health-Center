from django.db import models

# Create your models here.
class HospitalServices(models.Model):
    title = models.CharField(max_length=20, default="")
    availability = models.CharField(max_length=3, default="")
    Age = models.CharField(max_length=3, default="")
    Description = models.CharField(max_length=255, default="")
    Date = models.CharField(max_length=10, default="")
    Time = models.CharField(max_length=10, default="")
    
    
    
