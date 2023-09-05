from django.db import models

# Create your models here.
class bookingdb(models.Model):
    Name=models.CharField(max_length=30,null=True,blank=True)
    User=models.CharField(max_length=30,null=True,blank=True)
    Email=models.EmailField(max_length=30,null=True,blank=True)
    Date=models.CharField(max_length=30,null=True,blank=True)
    Chair=models.IntegerField(null=True,blank=True)
    Request=models.CharField(max_length=300,null=True,blank=True)
class userdb(models.Model):
    Name=models.CharField(max_length=30,null=True,blank=True)
    Email=models.EmailField(max_length=30,null=True,blank=True)
    Number=models.IntegerField(null=True,blank=True)
    Password=models.CharField(max_length=30,null=True,blank=True)

