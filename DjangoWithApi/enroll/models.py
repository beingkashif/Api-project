from django.db import models
# Create your models here.

class Student(models.Model):
     name = models.CharField(max_length=40)
     email = models.EmailField(max_length=40)
     password = models.CharField(max_length=20)
     gender = models.CharField(max_length=10)
     
     