from django.db import models

# Create your models here.
class Records(models.Model):
    ehrId = models.CharField(max_length=60, default="default")
    documentLink = models.CharField(max_length=255, default="default")
    created_at = models.CharField(max_length=10, default="00/00/00")