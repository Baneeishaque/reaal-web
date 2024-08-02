from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Login(models.Model):
    username = models.CharField(max_length=50,default='default_username')
    # ph = models.IntegerField()
    password = models.CharField(max_length=20)

    def __str__(self):
        return str(self.username)

class Registration(models.Model):
    name = models.CharField(max_length=50)
        # phon = models.IntegerField(max_length=15)
    email = models.EmailField(max_length=50)
        # address = models.CharField(max_length=50)
    password = models.CharField(max_length=150)
    # confirm_password = models.CharField(max_length=150)

    def __str__(self):
        return self.name
class Home(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # username = models.ForeignKey(User, on_delete=models.CASCADE)
    count = models.IntegerField(default=0)
    si_number = models.IntegerField(default=0)
    member_id = models.CharField(max_length=1000,unique=True,null=True,blank=True)
    # username = models.CharField(max_length=50)
    # username = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    left_customer = models.IntegerField(default=0)
    right_customer = models.IntegerField(default=0)
    amount = models.FloatField(default=0)
    # amount = models.DecimalField(max_digits=10, decimal_places=2,default=0.00)
    rebirth = models.BooleanField(default=False)

    def __str__(self):
        # return f"{self.username.username} - {self.si_number}"
        return self.user.username
        # return self.username
        # return f'{self.mobile_number} - {self.member_id}'
