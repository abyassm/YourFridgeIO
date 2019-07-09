from django.contrib import admin
from . models import Meat, Appetizer, Vegetable, Fruit, Recipe
# Register your models here
admin.site.register(Meat)
admin.site.register(Appetizer)
admin.site.register(Vegetable)
admin.site.register(Fruit)
admin.site.register(Recipe)
# admin.site.register(AddNewRecipe)
