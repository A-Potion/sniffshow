from django.urls import reverse
from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth import login
from django.views import generic
from .forms import SignUpForm, DogForm
from django.contrib.auth.decorators import login_required
from .models import UserData, Dog

@login_required
def profile(request):
    form = DogForm(request.POST or None)
    if form.is_valid():
        dog = form.save(commit=False)
        dog.user = request.user
        dog.save()
        form = DogForm()
        return HttpResponseRedirect(reverse("accounts:profile"))
    return render(request, "registration/profile.html", {"form": form})

def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            UserData.objects.create(user=user, phone=form.cleaned_data["phone"])
            login(request, user)
            return HttpResponseRedirect(reverse("event:list"))
    else:
        form = SignUpForm()
    return render(request, "registration/signup.html", {"form": form})