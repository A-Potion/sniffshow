from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from accounts.models import UserData

import datetime


class Event(models.Model):
    event_name = models.CharField(max_length=120)
    event_start_date = models.DateTimeField("event start date")
    event_end_date = models.DateTimeField("event end date")
    event_add_date = models.DateTimeField("event add date")
    event_price = models.PositiveIntegerField()
    event_description = models.TextField(max_length=1200)

    def event_already_happened(self):
        return self.event_end_date >= timezone.now()


class Application(models.Model):
    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
