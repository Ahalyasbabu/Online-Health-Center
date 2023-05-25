from django.db import models

# Create your models here.
class EHR(models.Model):
    patient_fname = models.CharField(max_length=20, default="")
    patient_lname = models.CharField(max_length=20, default="")
    email= models.CharField(max_length=20, default='default')
    ehr_status = models.CharField(max_length=10, default="")
    ehr_id = models.CharField(max_length=60, default= "")
    

