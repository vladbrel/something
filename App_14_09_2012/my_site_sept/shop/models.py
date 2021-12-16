from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=150)
    proce = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()

class Cover(models.Model):
    material = models.CharField(max_length=150)
    user = models.OneToOneField('User', on_delete=models.CASCADE)

class User(models.Model):
    title = models.CharField(max_length=150)


