from django.db import models

# Create your models here.
class categorydb(models.Model):
    Category_Name=models.CharField(max_length=30,null=True,blank=True)
    Description=models.CharField(max_length=300,null=True,blank=True)
    Image=models.ImageField(upload_to='Category',null=True,blank=True)

class productdb(models.Model):
    Category_Name=models.CharField(max_length=30,null=True,blank=True)
    Name=models.CharField(max_length=30,null=True,blank=True)
    Description=models.CharField(max_length=300,null=True,blank=True)
    Price=models.IntegerField(null=True,blank=True)
    Image=models.ImageField(upload_to='Category',null=True,blank=True)
