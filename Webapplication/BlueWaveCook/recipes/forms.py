from .models import Signup
from django import forms
from django.core import validators
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate

from django.contrib.auth.models import User
from django.conf import settings
import requests


class UserForm(forms.ModelForm):
  password = forms.CharField(label="Password", widget=forms.PasswordInput())
  passwordconfirm = forms.CharField(
      label="Password confirmation", widget=forms.PasswordInput())

  class Meta():
    model = User
    fields = ('first_name', 'last_name', 'username',
              'email', 'password', 'passwordconfirm')
  # this function will be used for the validation
  def clean(self):

    form_data = self.cleaned_data
    if form_data['password'] != form_data['passwordconfirm']:
        # Will raise a error message
        self._errors["password"] = ["Passwords do not match"]
        del form_data['password']
    return form_data


class UserLogin(AuthenticationForm):

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            self.user_cache = authenticate(
                username=username, password=password)
            if self.user_cache is None:
                raise forms.ValidationError(
                    ("Email ou Senha errados"))
            elif not self.user_cache.is_active:
                raise forms.ValidationError(("This account is inactive."))
        return self.cleaned_data


class RecipeForm(forms.Form):
    recipe = forms.CharField(max_length=150)

    def search(self):
        r = requests.get("https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/search?",
                         headers={
                             "X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
                             "X-RapidAPI-Key": "dd9d865db7mshfe856a8c5b93cf5p18212djsnb73b6d390fb9"
                         }
                         )
        print("The STATUS CODE IS: ", r.status_code)

        result = {}
        recipe = self.cleaned_data['recipe']
        print("Recipe searched is: ", recipe)
        # fill with api endpoint
        url = 'http://www.recipepuppy.com/api/?i=%s' % recipe
        print('searching the url: ', url)
        response = requests.get(url)

        print("The search code was: ", response)
        if response.status_code == 200:  # success
            result = response.json()
            print("api result is: ", result['title'])
            result['success'] = True
        else:
            result['success'] = False
            if response.status_code == 404:  # not found
                result['message'] = 'No entry for "%s"' % recipe
            else:
                result['message'] = 'The API is not available at the moment. Please try again later.'
        return result
