from django.db import models
import datetime

# Create your models here.


class Person(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, null=True)
    dob = models.CharField(max_length=255, null=True)
    file = models.FileField(upload_to="Files",null=True)
    shift = models.CharField(max_length=255, null=True)
    stime = models.CharField(max_length=255, null=True)
    etime = models.CharField(max_length=255, null=True)
    created_at = models.DateTimeField(max_length=255, null=True)
    updated_at = models.DateTimeField(max_length=255, null=True)



class Shift(models.Model):
    shift_name = models.CharField(max_length=30)
    stime = models.CharField(max_length=30)
    etime = models.CharField(max_length=30)


class Djangofrom(models.Model):
    name = models.CharField(max_length=30)
    age = models.CharField(max_length=30)


class Test(models.Model):
    user_id=models.CharField(max_length=50, null=True)


class User(models.Model):
    name = models.CharField(max_length=30, null=True)
    division = models.CharField(max_length=30, null=True)
    address = models.CharField(max_length=30, null=True)
    user = models.ForeignKey(Test, on_delete=models.CASCADE, null=True) #Foreign Key

















    