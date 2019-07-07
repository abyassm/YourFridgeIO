from django.db import models

# Create your models here.


class Appetier(models.Model):
    name = models.CharField(max_length=250)
    calories = models.IntegerField()
    weight = models.IntegerField()

    def __str__(self):
        return self.name


class Vegetable(models.Model):
    name = models.CharField(max_length=500)
    vegie_type = models.CharField(max_length=250)
    origin = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Fruit(models.Model):
    name = models.CharField(max_length=250)
    calories = models.IntegerField()

    def __str__(self):
        return self.name


class Meat(models.Model):
    name = models.CharField(max_length=250)
    meat_type = models.CharField(max_length=300)
    calories = models.IntegerField()
    weight = models.IntegerField()

    def __str__(self):
        return self.name


class Signup(models.Model):
    email = models.EmailField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
