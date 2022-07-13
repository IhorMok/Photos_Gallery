from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import TextInput, EmailInput, PasswordInput, EmailField


class RegisterUserForm(UserCreationForm):
    # email = forms.EmailField(attrs={'class': 'form-control', 'placeholder': 'Write Your Email'})

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password', 'password2']
        widgets = {
            'first_name': TextInput(attrs={'class': 'form-control input-md', 'placeholder': 'Write your First Name'}),
            'last_name': TextInput(attrs={'class': 'form-control input-md', 'placeholder': 'Write your Last Name'}),
            'email': EmailInput(attrs={'class': 'form-control', 'placeholder': 'Write Your Email'}),
            'password': PasswordInput(attrs={'class': 'form-control input-md', 'placeholder': 'Write Your Password'}),
        }
