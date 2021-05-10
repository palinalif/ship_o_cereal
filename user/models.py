from django.db import models
from django_countries.fields import CountryField
from django.contrib.auth.models import User
# Create your models here.

class Address(models.Model):
    country = CountryField()
    city = models.CharField(max_length=255)
    houseNumber = models.IntegerField()
    streetName = models.CharField(max_length=255)
    postNumber = models.IntegerField()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone = models.IntegerField()
    photo = models.CharField(max_length=999)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)

class PaymentInfo(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    cardHolder = models.CharField(max_length=255)
    cardNumber = models.IntegerField()
    expDate = models.IntegerField()
    cvc = models.IntegerField()

class SearchHistory(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    query = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add= True, blank= True)

class Order(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    status = models.CharField(max_length = 255)
    dateCreated = models.DateTimeField(auto_now_add = True)