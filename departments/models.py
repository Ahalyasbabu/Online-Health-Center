from django.db import models

# Create your models here.
class Departments(models.Model):
    name = models.CharField(max_length=15)
    description =models.CharField(max_length=50)
    img = models.ImageField(upload_to='appUploads', default=None)
    def __str__(self):
        return self.name

    

