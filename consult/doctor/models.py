from django.db import models
from departments.models import Departments

# Create your models here.
class Doctor(models.Model):
    name = models.CharField(max_length=20)
    lname = models.CharField(max_length=20, default="")
    qualification = models.CharField(max_length=30)
    img = models.ImageField(upload_to='appUploads', default=None)
    availability = models.BooleanField()
    email=models.CharField(max_length=20, default='default')
    password=models.CharField(max_length=20, default='default')
    year_of_experience = models.IntegerField()
    department = models.ForeignKey(Departments, on_delete=models.CASCADE)
    def __str__(self):
        return self.name


# class TimeSlots(models.Model):
#     timeSlot= models.CharField(max_length=20)
#     dateSlot= models.CharField(max_length=10)
#     availability= models.CharField(max_length=10)
#     doctorId = models.ForeignKey(Docotrs, on_delete=models.CASCADE)