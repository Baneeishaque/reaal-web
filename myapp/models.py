from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Login(models.Model):
    user_name = models.CharField(max_length=50,default='default_username')
    # ph = models.IntegerField()
    password = models.CharField(max_length=20)

    def __str__(self):
        return str(self.user_name)
class Home(models.Model):
# class CustomUser(AbstractUser):
# class UserProfile(models.Model):

    mobile_number = models.CharField(max_length=15,unique=True)
    member_id = models.CharField(max_length=50)
    left_customer = models.IntegerField(default=0)
    right_customer = models.IntegerField(default=0)
    amount = models.FloatField(default=0)
    rebirth = models.BooleanField(default=False)
    income = models.FloatField(default=0)
    count = models.IntegerField()
    # si_no = models.IntegerField()
    si_no = models.AutoField(primary_key=True)
    # formatted_date = models.CharField(max_length=20)
    formatted_date = models.DateField()

    def __str__(self):
        # return str(self.si_no)
        return str(self.member_id)
        # return f'{self.mobile_number} - {self.member_id}'
