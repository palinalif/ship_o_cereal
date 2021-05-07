from django.db import models
from django_countries.fields import CountryField

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)
    phone = models.IntegerField()
    photo = models.CharField(max_length=999)
    streetname = models.CharField(max_length=255)
    houseNumber = models.IntegerField()
    postNumber = models.IntegerField()
    city = models.CharField(max_length=255)
    country = CountryField()