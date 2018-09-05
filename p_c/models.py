from django.db import models

# Create your models here.

class Account(models.Model):
    Account_No = models.AutoField(primary_key=True)
    Name = models.CharField(max_length= 20)
    Address = models.CharField(max_length= 40)
    Location = models.CharField(max_length=30)
    Pin = models.CharField()
    State = models.CharField(max_length=20)
    City = models.CharField(max_length= 20)
    Country = models.CharField(max_length= 20)
