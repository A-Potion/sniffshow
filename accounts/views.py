from django.urls import reverse_lazy
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.views import generic


# Create your views here.
class SignUpView(generic.CreateView):
    form = UserCreationForm()
    success_url = reverse_lazy("event:list")
    template_name = "registration/signup.html"