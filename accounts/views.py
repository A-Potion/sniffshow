from django.urls import reverse
from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.views import generic
from .forms import SignUpForm
from django.contrib.auth.models import UserManager


def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user_manager = UserManager()
            user_manager.create_user(username=user.username, email=user.email, password=user.password1)
            login(request, user)
            return HttpResponseRedirect(reverse("event:list"))
    else:
        form = SignUpForm()
    return render(request, "registration/signup.html", {"form": form})