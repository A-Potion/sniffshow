from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from accounts.models import UserData, Dog

import datetime


class Event(models.Model):
    added_by = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    event_name = models.CharField(max_length=120)
    event_start_date = models.DateTimeField("event start date")
    event_end_date = models.DateTimeField("event end date")
    event_add_date = models.DateTimeField("event add date")
    event_price = models.PositiveIntegerField()
    event_description = models.TextField(max_length=1200)
    applications_deadline = models.DateTimeField("applications deadline")

    def event_already_happened(self):
        return self.event_end_date >= timezone.now()

    def applications_closed(self):
        return self.applications_deadline >= timezone.now()


class Application(models.Model):
    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    dogs = models.ManyToManyField(Dog)

    notes = models.TextField(max_length=500)