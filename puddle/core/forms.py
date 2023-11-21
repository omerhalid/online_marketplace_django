from django import forms

from django.contrib.auth.forms import UserCreationForm # This is a built-in form from Django.
from django.contrib.auth.models import User # This is a built-in model from Django.

class SignupForm(UserCreationForm): # This is a form that inherits from the UserCreationForm.
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'w-full py-4 px-6 rounded-xl', 'placeholder': 'Username'})) # This is a field that inherits from the CharField. It has a widget that inherits from the TextInput. It has a class attribute that is a string. It has a placeholder attribute that is a string.
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'w-full py-4 px-6 rounded-xl', 'placeholder': 'Email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'w-full py-4 px-6 rounded-xl', 'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'w-full py-4 px-6 rounded-xl', 'placeholder': 'Repeat Password'}))