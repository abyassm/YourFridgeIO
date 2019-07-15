# from appname.assets.blocked_emails import disposable_emails
from django.shortcuts import render, redirect
import requests
from . import forms
# from django import forms
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Recipe
from django.db.models import Q
from django.contrib.auth.models import User
# Create your views here.

# Create your views here.

def index(request):

  return render(request, 'recipes/index.html')


def about(request):
    return render(request, 'recipes/about.html')


def contact(request):
    return render(request, 'recipes/contact.html')


def footer(request):
    return render(request, 'recipes/footer.html')


def login_user(request):
  if request.method == "POST":
    username = request.POST.get('username')
    password = request.POST.get('password')

    user = authenticate(username=username, password=password)

    if user:
        if user.is_active:
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            HttpResponse("Account not active!")
    else:
        print("someone tried to login and failed!")
        print("username: {} and password {}".format(username, password))
        # raise forms.ValidationError('Email já em uso')
        # raise ValidationError("Sorry, that login was invalid. Please try again.")
        messages.error(
            request, 'Sorry, Username or Password Incorrect. Please try again.')
        return redirect('/login/')
        # return render(request, 'globalkitchen/login.html', {"err":"Sorry, that login was invalid. Please try again."})
  else:

     return render(request, 'recipes/login.html', {})


def signup_user(request):
  registered = False
  if request.method == 'POST':
    user_form = forms.UserForm(data=request.POST)

    if user_form.is_valid():
      user = user_form.save()
      user.set_password(user.password)
      user.save()
      registered = True
      login(request, user)
      return HttpResponseRedirect(reverse('index'))
    else:
        print(user_form.errors)
  else:
      user_form = forms.UserForm()

  return render(request, 'recipes/signup.html', {'user_form': user_form, 'registered': registered})


@login_required
def logout_user(request):
	logout(request)
	return HttpResponseRedirect(reverse('index'))


# # def recipes(request):
#     search_result = {}
#     if 'recipe' in request.GET:
#         form = forms.RecipeForm(request.GET)
#         if form.is_valid():
#             search_result = form.search()
#     else:
#         form = forms.RecipeForm()
#     return render(request, 'recipes/recipes.html', {'form': form, 'search_result': search_result})


def recipes(request):
    if request.method == 'GET':
        query = request.GET.get('q')


        submitbutton = request.GET.get('submit')

        if query is not None:
              
              
              if request.GET.get('searchType') == 'byRecipe':
                     lookups = Q(name__icontains=query)
                     results = Recipe.objects.filter(lookups).distinct()
              elif request.GET.get('searchType') == 'byIngredients':
                     lookups = Q(ingredients__icontains=query)
                     results = Recipe.objects.filter(lookups).distinct()
              elif request.GET.get('searchType') == 'ByFridge':
                     arr1 = query.split(", ")
                     inputCount = len(arr1)
                     #find recipes with set amount of ingredients or less
                     lookups = Q(ingredientCount__lte=inputCount)
                     results1 = Recipe.objects.filter(lookups).distinct()
                     #
                     flag = 1
                     counter = 0
                     results = []
                     for x in results1:
                           #Work in progress
                           flag = 1
                           ingredientsArr = x.ingredients.split(", ")
                           for i in range(0, len(ingredientsArr)):
                                 for y in range(0,len(arr1)):
                                       if ingredientsArr[i] != arr1[y]:
                                             flag = 1
                                       elif ingredientsArr[i] == arr1[y]:
                                             flag = 0
                                             break
                           if flag == 0:
                                 results.append(x)
                                 counter = counter + 1

                                             

              

              


              context = {'results': results,
                          'submitbutton': submitbutton}
              
                   
          

              return render(request, 'recipes/recipes.html', context)

        else:
            return render(request, 'recipes/recipes.html')

    else:
        return render(request, 'recipes/recipes.html')


@login_required(login_url='/login/')
def form_view(request):

    form = forms.NewRecipe(request.POST, request.FILES)

    if request.method == 'POST':
        form = forms.NewRecipe(request.POST, request.FILES)

        if form.is_valid():
            recipe_name = form.cleaned_data['name']
            recipe_image = form.cleaned_data['image']
            recipe_ingredients = form.cleaned_data['ingredients']
            recipe_calories = form.cleaned_data['calories']
            recipe_instructions = form.cleaned_data['instructions']

            arr = recipe_ingredients.split(', ')
            arrCount = len(arr)

            new_recipe = Recipe(name=recipe_name, image=recipe_image, ingredients=recipe_ingredients, calories=recipe_calories,
                                instructions=recipe_instructions, ingredientCount=arrCount)


            
            new_recipe.save()

            print("Validation success!")
            # redirect, i want to update this so that it goes to the beer lists page later
            # return HttpResponse("Recipe added. Thank you")
            return HttpResponseRedirect(reverse('index'))
    else:
        form = forms.NewRecipe()
    return render(request, 'recipes/addrecipe.html', {'form': form})
