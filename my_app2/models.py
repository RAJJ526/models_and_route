from django.db import models

# Create your models here.
class Voicebar(models.Model):
    name=models.CharField(max_length=100)
    age=models.SmallIntegerField()
    role=models.CharField(max_length=100, default="none")
    salary=models.IntegerField()

class Accountant(models.Model):
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

class Clerk(models.Model):
    name=models.CharField(max_length=100)
    age=models.SmallIntegerField()
    Salary=models.IntegerField()

class Manager(models.Model):
    name=models.CharField(max_length=100)
    age=models.SmallIntegerField()
    Salary=models.IntegerField()

class Cashier(models.Model):
    name=models.CharField(max_length=100)
    age=models.SmallIntegerField()
    Salary=models.IntegerField()

class Designer(models.Model):
    name=models.CharField(max_length=100)
    age=models.SmallIntegerField()
    Salary=models.IntegerField()

class Guard(models.Model):
    name=models.CharField(max_length=100)
    age=models.SmallIntegerField()
    Salary=models.IntegerField()

class HR(models.Model):
    name=models.CharField(max_length=100)
    age=models.SmallIntegerField()
    Salary=models.IntegerField()