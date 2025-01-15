from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    usertype = models.CharField(max_length=30)
    is_approved = models.CharField(max_length=10)
class Teacher(models.Model):
    teach = models.ForeignKey(User,on_delete=models.CASCADE)
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    emailid = models.EmailField()
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
class Student(models.Model):
    stud = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    department = models.CharField(max_length=30)
    phoneno = models.IntegerField()
    emailad = models.EmailField()
    studuser = models.CharField(max_length=30)
    studpwd = models.CharField(max_length=30)
