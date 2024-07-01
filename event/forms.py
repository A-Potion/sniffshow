from django import forms

class AddForm(forms.Form):
    ename = forms.CharField(label="Event name", max_length=120)