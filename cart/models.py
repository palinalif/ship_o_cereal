from django.db import models
from products.models import Product
from user.models import Order

# Create your models here.

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete = models.CASCADE)
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    quantity = models.IntegerField()