from django.db import models

# Create your models here.
class Consumer(models.Model):
    name = models.CharField(max_length=20, default="default")
    hospitalId = models.CharField(max_length=20, default="default")
    email = models.CharField(max_length=20, default="default")
    ehrId = models.CharField(max_length=60, default="default")



