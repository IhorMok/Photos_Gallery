from django import forms
from django.contrib.auth.forms import UserCreationForm

from django.forms import TextInput, EmailInput, PasswordInput, EmailField, CharField

from gallery.models import User


class RegisterUserForm(UserCreationForm):
    first_name = CharField(
        required=True,
        widget=TextInput(
            attrs={
                'class': 'form-control input-md', 
                'placeholder': 'Write your First Name'
            }
        )
    )
    last_name = CharField(
        widget=TextInput(
            attrs={
                'class': 'form-control input-md', 
                'placeholder': 'Write your Last Name'
            }
        )
    )
    email = EmailField(
        widget=EmailInput(
            attrs={
                'class': 'form-control', 
                'placeholder': 'Write Your Email'
                }
        )
    )
    password1 = CharField(
        widget=PasswordInput(
            attrs={
                'class': 'form-control input-md', 
                'placeholder': 'Write Your Password', 
            }
        )
    )
    password2 = CharField(
        widget=PasswordInput(
            attrs={
                'class': 'form-control input-md', 
                'placeholder': 'Confirm Password', 
            }
        )
    )

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2']