from django.db import models
from cart.models import OrderItem

# Create your models here.

class Address(models.Model):
    addressID = models.UUIDField()
    country = models.CharField()
    city = models.CharField()
    houseNumber = models.IntegerField()
    streetName = models.CharField()
    postNumber = models.IntegerField()

class User(models.Model):
    userID = models.UUIDField()
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)
    phone = models.IntegerField(max_length=7)
    photo = models.CharField(max_length=999)
    address = models.ForeignKey(Address, on_delete= models.CASCADE)

class PaymentInfo(models.Model):
    userID = models.ForeignKey(User, on_delete=models.CASCADE)
    cardHolder = models.CharField(max_length=255)
    cardNumber = models.IntegerField(max_length=16)
    expDate = models.IntegerField(max_length=16)
    cvc = models.IntegerField(max_length=3)

class SearchHistory(models.Model):
    userID = models.ForeignKey(User, on_delete=models.CASCADE)
    query = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add= True, blank= True)

class Orders(models.Model):
    userID = models.ForeignKey(User, on_delete=models.CASCADE)
    orderID = models.ForeignKey(OrderItem, on_delete=models.CASCADE)