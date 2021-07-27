from django.db import models
from datetime import datetime


# Create your models here.
class Recipe(models.Model):
    name = models.CharField(max_length=250)
    calories = models.IntegerField()
    image = models.ImageField()
    ingredients = models.CharField(max_length=1000)
    instructions = models.CharField(max_length=1500)
    ingredientCount = models.IntegerField()

    def __str__(self):
        
         return self.name
class Rating(models.Model):
    recipe = models.CharField(max_length=250)
    user = models.CharField(max_length=250)
    rating = models.IntegerField()

class Signup(models.Model):
    email = models.EmailField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
