from django.db import models

# Create your models here.
class Medicine(models.Model):
    name = models.CharField(max_length=40, default="")
    price = models.CharField(max_length=10, default="")
    inStock = models.CharField(max_length=10, default="")
    provider = models.CharField(max_length=10, default="")
    manufacturing_date = models.CharField(max_length=10, default="")
    availablity = models.CharField(max_length=10, default="")
    description = models.CharField(max_length=80, default="")
    more = models.CharField(max_length=80, default="")
    expiration_date = models.CharField(max_length=80, default="")