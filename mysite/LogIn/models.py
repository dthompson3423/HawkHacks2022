from django.db import models

# Create your models here.
class User_Login(models.Model):
    #firstName = models.CharField(max_length=60)
    #lastName = models.CharField(max_length=60)
    email = models.CharField(max_length=100)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    unlocked = models.IntegerField(default = 1) # Range from 1 to 3 to see how many videos user has unlocked
