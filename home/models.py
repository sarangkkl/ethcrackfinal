from django.db import models

# Create your models here.
class CrytoAcc(models.Model):
    address = models.CharField(max_length=200,blank=True,null=True)
    balance = models.CharField(max_length=20,blank=True,null=True)

    def __str__(self):
        return self.address

class MoneyAcc(models.Model):
    private_key = models.CharField(max_length=100,blank=True,null=True)
    public_key = models.CharField(max_length=100,blank=True,null=True)
    blance = models.CharField(max_length=20,blank=True,null=True)

    def __str__(self):
        return self.public_key
