from django import forms

from django.contrib.auth.forms import UserCreationForm # This is a built-in form from Django.
from django.contrib.auth.models import User # This is a built-in model from Django.

class SignupForm(UserCreationForm): # This is a form that inherits from the UserCreationForm.
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')