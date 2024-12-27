from django.db import models

# Create your models here.
class person(models.Model):
    email=models.EmailField()
    password=models.CharField(max_length=25)
    class Meta:
        db_table="person"

class Product(models.Model):
    name = models.CharField(max_length=15)
    price = models.DecimalField(max_digits=8,decimal_places=2)
    description = models.TextField()
    class Meta:
        db_table="Product"

def get_default_email():
    return "abc@gmail.com"

class NewCartItems(models.Model):
    email = models.EmailField(default=get_default_email)
    name = models.CharField(max_length=15)
    price = models.DecimalField(max_digits=8,decimal_places=2)
    class Meta:
        db_table="NewCartItems"

class ItemsPurchased(models.Model):
    email = models.EmailField(default=get_default_email)
    name = models.CharField(max_length=15)
    price = models.DecimalField(max_digits=8,decimal_places=2)
    class Meta:
        db_table="ItemsPurchased"

