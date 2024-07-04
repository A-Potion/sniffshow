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
from .forms import AddForm


import datetime

class ListView(generic.ListView):
    template_name = "event/list.html"
    context_object_name = "events_to_happen"
    def get_queryset(self):
        return Event.objects.filter(event_end_date__gte = timezone.now()).order_by("-event_end_date")
    
class DetailView(generic.DetailView):
    model = Event
    template_name = "event/detail.html"


def add(request):
    error_msg = ""
    if request.method == "POST":
        form = AddForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            event_start_date = form.cleaned_data["event_start_date"]
            event_end_date = form.cleaned_data["event_end_date"]
            event_name = form.cleaned_data["event_name"]
            event_price = form.cleaned_data["event_price"]
            if event_end_date <= event_start_date:
                error_msg = "The event may not end before it starts."
            else:
                Event.objects.create(event_add_date=timezone.now(), event_start_date=event_start_date, event_end_date=event_end_date, event_name=event_name, event_price=event_price)
                return HttpResponseRedirect(reverse("event:list"))
    else:
        form = AddForm()
        
    return render(request, "event/add.html", {"form": form, "error_msg": error_msg})