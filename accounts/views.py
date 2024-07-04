from django.urls import reverse_lazy
from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from .forms import SignUpForm
from django.contrib.auth import login

def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return HttpResponseRedirect(reverse("event:list"))
    else:
        form = SignUpForm()
    return render(request, "registration/signup.html", {"form": form})