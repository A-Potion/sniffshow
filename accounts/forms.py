from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserData

class SignUpForm(UserCreationForm):
    phone = forms.CharField(max_length=15)
    email = forms.EmailField(max_length=200)

    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + ("password1", "password2", "email", "phone")
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'password1': forms.PasswordInput(attrs={'placeholder': 'Password'}),
            'password2': forms.PasswordInput(attrs={'placeholder': 'Repeat password'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Phone number'}),
        }
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        for name, widget in self._meta.widgets.items():
            self[name].field.widget.attrs.update(widget.attrs)
