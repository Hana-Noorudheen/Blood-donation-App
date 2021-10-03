from django.db import models

# Create your models here.

class donor_details(models.Model):
    Name=models.CharField(max_length=30)
    Age=models.IntegerField()
    Gender=models.CharField(max_length=20)
    BloodGroup=models.CharField(max_length=5)
    City=models.CharField(max_length=20)
    Phone=models.CharField(max_length=13)
    Email=models.EmailField()

class img(models.Model):
    Img=models.ImageField(upload_to='pics')
    





    











