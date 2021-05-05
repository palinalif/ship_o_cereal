from django.db import models
from products.models import Product
from register.models import Order

# Create your models here.

class OrderItem(models.Model):
    order = models.ForeignKey(Order)
    product = models.ForeignKey(Product)
    quantity = models.IntegerField()