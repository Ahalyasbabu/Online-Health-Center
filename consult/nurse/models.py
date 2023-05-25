from django.db import models

# Create your models here.
class Nurse(models.Model):
    name = models.CharField(max_length=20)
    lname = models.CharField(max_length=20, default="")
    qualification = models.CharField(max_length=30)
    availability = models.BooleanField()
    email=models.CharField(max_length=20, default='default')
    password=models.CharField(max_length=20, default='default')
    year_of_experience = models.IntegerField()
    