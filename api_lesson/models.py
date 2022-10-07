from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    price = models.IntegerField()
