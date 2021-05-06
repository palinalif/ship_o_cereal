from django.db import models

# Create your models here.

class Address(models.Model):
    addressID = models.UUIDField()
    country = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    houseNumber = models.IntegerField()
    streetName = models.CharField(max_length=255)
    postNumber = models.IntegerField()

class User(models.Model):
    userID = models.UUIDField()
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)
    phone = models.IntegerField()
    photo = models.CharField(max_length=999)
    address = models.ForeignKey(Address, on_delete= models.CASCADE)

class PaymentInfo(models.Model):
    userID = models.ForeignKey(User, on_delete=models.CASCADE)
    cardHolder = models.CharField(max_length=255)
    cardNumber = models.IntegerField()
    expDate = models.IntegerField()
    cvc = models.IntegerField()

class SearchHistory(models.Model):
    userID = models.ForeignKey(User, on_delete=models.CASCADE)
    query = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add= True, blank= True)

class Order(models.Model):
    userID = models.ForeignKey(User, on_delete=models.CASCADE)
    orderID = models.UUIDField()
    status = models.CharField(max_length = 255)
    dateCreated = models.DateTimeField(auto_now_add = True)