from django.db import models

# Create your models here.

class Man(models.Model):
    name= models.CharField(max_length=50)
    age = models.DecimalField(max_digits=3, decimal_places=0)
    sex = models.CharField(max_length=50)


class Passport(models.Model):
    series = models.CharField(max_length=2)
    number = models.DecimalField(max_digits=10, decimal_places=0)
    id_number = models.CharField(max_length=20)
    man = models.OneToOneField(Man, on_delete= models.CASCADE, primary_key=True)

# class Man(models.Model):
#     name= models.CharField(max_length=50)
#     age = models.DecimalField(max_digits=3, decimal_places=0)
#     sex = models.CharField(max_length=50)
#
# class Passport(models.Model):
#     series = models.CharField(max_length=2)
#     number = models.DecimalField(max_digits=10, decimal_places=0)
#     id_number = models.CharField(max_length=20)
#     man = models.OneToOneField('Man', on_delete=models.CASCADE)
