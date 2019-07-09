from django.db import models
from datetime import datetime


# Create your models here.
class AddNewRecipe(models.Model):
    title = models.CharField(max_length=550)
    image = models.ImageField(upload_to='photos')
    ingredients = models.CharField(max_length=5500)
    preparation = models.CharField(max_length=5500)
    tips = models.CharField(max_length=550)
    nutrition = models.CharField(max_length=550)

    def __str__(self):
        return self.title


class Recipe(models.Model):
    name = models.CharField(max_length=250)
    calories = models.IntegerField()
    image = models.ImageField(upload_to="recipes/static/images")
    ingredients = models.CharField(max_length=1000)
    instructions = models.CharField(max_length=1500)
    def __str__(self):
        
         return self.name



class Appetizer(Recipe):
    
    pass

class Vegetable(Recipe):
    
    pass
class Fruit(Recipe):
    pass

class Meat(Recipe):
    pass


class Signup(models.Model):
    email = models.EmailField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
