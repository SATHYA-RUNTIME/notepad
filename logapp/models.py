from django.db import models

# Create your models here.
class register(models.Model):
    username=models.CharField(max_length=50,primary_key = True)
    mobileno=models.TextField()
    age=models.CharField(max_length=50)
    gender=models.CharField(max_length=50)
    mail=models.CharField(max_length=50)
    nikename=models.CharField(max_length=50)
    pwd=models.CharField(max_length=20)
    
   
class data(models.Model):
    npuname=models.CharField(max_length=50)
    npnots=models.TextField()
    date=models.CharField( max_length=50)
    time=models.CharField(max_length=50)
