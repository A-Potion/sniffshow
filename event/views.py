from multiprocessing.reduction import register

from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Event
from django.http import Http404
from django.db.models import F
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.contrib.auth import views as auth_view
from .forms import AddForm, ApplyForm
from django.contrib.auth.decorators import login_required


import datetime

class ListView(generic.ListView):
    template_name = "event/list.html"
    context_object_name = "events_to_happen"
    def get_queryset(self):
        return Event.objects.filter(event_end_date__gte = timezone.now()).order_by("event_start_date")
    
class DetailView(generic.DetailView):
    model = Event
    template_name = "event/detail.html"

@login_required
def apply(request, pk):
    if request.method == "POST":
        form = super().get_form(ApplyForm)  # Get the form as usual
        user = self.request.user
        form.fileds['dogs'].queryset = Dog.objects.filter(user=user)
        if form.is_valid():
            form.clean()
            application = form.save(commit=False)
            application.user = request.user
            application.save()
            return HttpResponseRedirect(reverse("event:list"))
    else:
        form = ApplyForm()
    return render(request, "event/apply.html", {"form": form})

@login_required
def add(request):
    error_msg = ""
    if request.method == "POST":
        form = AddForm(request.POST)
        if form.is_valid():
            form.clean()
            event = form.save(commit=False)
            event.event_add_date = timezone.now()
            event.added_by = request.user
            event_end_date = form.cleaned_data["event_end_date"]
            event_start_date = form.cleaned_data["event_start_date"]
            if event_end_date <= event_start_date:
                error_msg = "The event may not end before it starts."
            else:
                event.save()
                return HttpResponseRedirect(reverse("event:list"))
    else:
        form = AddForm()
        
    return render(request, "event/add.html", {"form": form, "error_msg": error_msg})