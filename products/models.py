from django.db import models

# Create your models here.

class ProductManufacturer(models.Model):
    name = models.CharField(max_length = 255)

    def __str__(self):
        return self.name

class ProductTag(models.Model):
    name = models.CharField(max_length = 255)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length = 255)
    manufacturer = models.ForeignKey(ProductManufacturer, on_delete = models.CASCADE)
    price = models.IntegerField()
    description = models.CharField(max_length = 255, blank = True)
    nutriInfo = models.CharField(max_length = 255, blank = True)
    amount = models.IntegerField()
    tag = models.ForeignKey(ProductTag, on_delete = models.CASCADE)

class ProductImage(models.Model):
    image = models.CharField(max_length = 9999)
    product = models.ForeignKey(Product, on_delete = models.CASCADE)