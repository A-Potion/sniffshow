from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Event
from django.http import Http404
from django.db.models import F
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .forms import AddForm


class ListView(generic.ListView):
    template_name = "event/list.html"
    context_object_name = "events_to_happen"
    def get_queryset(self):
        return Event.objects.filter(event_end_date__gte = timezone.now()).order_by("-event_end_date")

def add(request):
    if request.method == "POST":
        form = AddForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect(reverse("event:list"))
    else:
            form = AddForm()
        
    return render(request, "add.html", {"form": form})