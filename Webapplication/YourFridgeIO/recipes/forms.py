
from django import forms
from django.core import validators
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate

from django.contrib.auth.models import User
from django.conf import settings
import requests
from .models import Recipe

"""
Authors:
    Ryan Jiffri
    Abdirahman Yassin
    Faiq Ahmed
    Jules Mbende Bong

"""

class NewRecipe(forms.ModelForm):
    count = 0
    class Meta():
        model = Recipe
        fields = ('name', 'calories', 'image', 'ingredients', 'instructions',)
        
        

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
                    ("Email error"))
            elif not self.user_cache.is_active:
                raise forms.ValidationError(("This account is inactive."))
        return self.cleaned_data
