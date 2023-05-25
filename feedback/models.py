from django.db import models

# Create your models here.
class FeedBack(models.Model):
    userName = models.CharField(max_length=20, default="")
    userEmail = models.CharField(max_length=20, default="")
    doctorId = models.CharField(max_length=10, default="")
    doctorName = models.CharField(max_length=20, default="")
    rating = models.CharField(max_length=10, default="")
    description = models.CharField(max_length=10, default="")
    viwedByDoctor = models.CharField(max_length=10, default="")
    viwedByAdmin = models.CharField(max_length=10, default="")
