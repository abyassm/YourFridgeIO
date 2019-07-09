from django.db import models
from datetime import datetime


# Create your models here.
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
