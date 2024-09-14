from django.db import models

# Create your models here.
class Company(models.Model):
    name=models.CharField(max_length=100, blank=True)
    age=models.SmallIntegerField()
    role=models.CharField(max_length=100, default="none")
    salary=models.IntegerField()

class Salesman(models.Model):
    name=models.CharField(max_length=100)
    age=models.SmallIntegerField()
    Salary=models.IntegerField()

class Engineer(models.Model):
    name=models.CharField(max_length=100)
    age=models.SmallIntegerField()
    Salary=models.IntegerField()

class Analyst(models.Model):
    name=models.CharField(max_length=100)
    age=models.SmallIntegerField()
    Salary=models.IntegerField()

class Programmer(models.Model):
    name=models.CharField(max_length=100)
    age=models.SmallIntegerField()
    Salary=models.IntegerField()

class System_Analyst(models.Model):
    name=models.CharField(max_length=100)
    age=models.SmallIntegerField()
    Salary=models.IntegerField()

class Web_developer(models.Model):
    name=models.CharField(max_length=100)
    age=models.SmallIntegerField()
    Salary=models.IntegerField()

class Designer(models.Model):
    name=models.CharField(max_length=100)
    age=models.SmallIntegerField()
    Salary=models.IntegerField()

class SEO(models.Model):
    name=models.CharField(max_length=100)
    age=models.SmallIntegerField()
    Salary=models.IntegerField()

class HR(models.Model):
    name=models.CharField(max_length=100)
    age=models.SmallIntegerField()
    Salary=models.IntegerField()