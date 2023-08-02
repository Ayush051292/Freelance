from django.db import models

# Create your models here.


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50, null=True)
    dob = models.CharField(max_length=100, null=True)
    country = models.CharField(max_length=100, null=True)
    file = models.FileField(upload_to="Files",null=True)






    