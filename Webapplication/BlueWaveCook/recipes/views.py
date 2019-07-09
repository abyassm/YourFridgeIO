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
# from . models import AddNewRecipe
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
            lookups = Q(name__icontains=query)

            results = Recipe.objects.filter(lookups).distinct()

            context = {'results': results,
                       'submitbutton': submitbutton}

            return render(request, 'recipes/recipes.html', context)

        else:
            return render(request, 'recipes/recipes.html')

    else:
        return render(request, 'recipes/recipes.html')