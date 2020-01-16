from django.db import models

# Create your models here.

class Product(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=20)

class Type(models.Model):
    id = models.AutoField(primary_key=True)
    type_name = models.CharField(max_length=20)