from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserData, Dog
from django.core.exceptions import ValidationError

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

class DogForm(forms.ModelForm):
    class Meta:
        model = Dog
        fields = ["sex", "name"]
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Name'}),
            'sex': forms.Select(),
        }

    def clean(self):
        cleaned_data = self.cleaned_data

        try:
            Dog.objects.get(name=cleaned_data['name'], user=self.user)
        except Dog.DoesNotExist:
            pass
        else:
            raise ValidationError('Solution with this Name already exists for this problem')

        # Always return cleaned_data
        return cleaned_data