from django import forms
from django.forms import ModelForm
from django.http import request
from django.contrib.auth.models import User

from .models import Event, Application
from django.contrib.auth.models import User

class DateTimeInput(forms.DateTimeInput):
    input_type = 'datetime-local'

class AddForm(ModelForm):
    class Meta:
        model = Event
        fields = ["event_name", "event_description", "event_start_date", "event_end_date", "event_price", "applications_deadline"]
        widgets = {
            'event_start_date': DateTimeInput(),
            'event_end_date': DateTimeInput(),
            'applications_deadline': DateTimeInput(),
        }

class ApplyForm(ModelForm):
    class Meta:
        model = Application
        fields = ["dogs", "notes"]