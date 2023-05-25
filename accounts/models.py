from django.db import models

# Create your models here.
class UserAccount(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    img = models.TextField()
    # img = models.ImageField(upload_to='appUploads', default=None)
    