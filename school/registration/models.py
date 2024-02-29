from django.db import models

# Create your models here.

class department(models.Model):
    title=models.CharField(max_length=50)

class student(models.Model):
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    age=models.CharField(max_length=3)
    department=models.ForeignKey(department,on_delete=models.CASCADE)