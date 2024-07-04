from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django.forms import TextInput, EmailInput, PasswordInput, ModelForm

class SignUpForm(ModelForm):
    email = forms.EmailField(max_length=200, help_text="w")

    class Meta:
        model = CustomUser
        fields = ["username", "email", "password1", "password2"]
        widgets = {
            'username': TextInput(attrs={'placeholder': 'Username'}),
            'email': EmailInput(attrs={'placeholder': 'Email'}),
            'password1': PasswordInput(attrs={'placeholder': 'Password'}),
            'password2': PasswordInput(attrs={'placeholder': 'Repeat password'}),
        }