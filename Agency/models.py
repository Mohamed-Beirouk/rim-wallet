from email.policy import default
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Account(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default="")
    Balance = models.FloatField()
    Entitled = models.CharField(max_length=30, unique=True) 
    CreationDate = models.DateTimeField(auto_now_add=True)
    Login = models.CharField(max_length=10)
    Password = models.CharField(max_length=4)
    currency = models.CharField(max_length=30, default="MRU") 
    class Meta:
        unique_together = ('Login', 'Password',)

    def __str__(self):
        return self.user.first_name
        

class Transaction(models.Model):
    Account = models.ForeignKey(Account, on_delete=models.CASCADE)
    TransactionId = models.CharField(max_length=30, unique=True)
    Note = models.CharField(max_length=100, blank=True, null=True)
    TransactionDate = models.DateTimeField(auto_now_add=True)
    CustomerFullName = models.CharField(max_length=50)
    Output = models.FloatField(blank=True, null=True)
    Input = models.FloatField(blank=True, null=True)
    Currency = models.FloatField()
    Credit = models.FloatField()
    recu = models.CharField(max_length=10 ,default="False")
    
    def __str__(self):
        return self.Account.user.first_name