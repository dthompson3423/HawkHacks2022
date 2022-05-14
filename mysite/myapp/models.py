from django.db import models

# Create your models here.
class User_Login(models.Model):
    email = models.CharField(max_length=100)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    