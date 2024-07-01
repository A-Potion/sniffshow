from django import forms
from django.forms import ModelForm
from .models import Event

class DateInput(forms.DateTimeInput):
    input_type = 'datetime-local'

class AddForm(ModelForm):
    class Meta:
        model = Event
        fields = ["event_name", "event_start_date", "event_end_date", "event_price"]
        widgets = {
            'event_start_date': DateInput(),
            'event_end_date': DateInput(),
        }