from django.urls import reverse
from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth import login
from django.views import generic
from .forms import SignUpForm, DogForm
from django.contrib.auth.decorators import login_required
from .models import UserData, Dog
from django.core.exceptions import ValidationError

@login_required
def profile(request):
    form = DogForm(request.POST or None)
    dog = form.save(commit=False)
    dog.user = request.user
    if form.is_valid():
        try:
            dog.clean()
            dog.save()
            form = DogForm()  # Reset the form after saving
            return HttpResponseRedirect(reverse("accounts:profile"))
        except ValidationError as e:
            # Handle the validation error, e.g., by adding it to the form's errors
            form.add_error(None, e)
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