from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import TextInput, EmailInput, PasswordInput, ModelForm, EmailField

class SignUpForm(UserCreationForm):
    email = EmailField(max_length=200)

    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + ("password1", "password2", "email")
        widgets = {
            'username': TextInput(attrs={'placeholder': 'Username'}),
            'email': EmailInput(attrs={'placeholder': 'Email'}),
            'password1': PasswordInput(attrs={'placeholder': 'Password'}),
            'password2': PasswordInput(attrs={'placeholder': 'Repeat password'}),
        }