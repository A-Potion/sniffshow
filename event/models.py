from django.utils import timezone
from django.db import models

import datetime

class Event(models.Model):
    event_name = models.CharField(max_length=120)
    event_start_date = models.DateTimeField("event start date")
    event_end_date = models.DateTimeField("event end date")
    event_add_time = timezone.now()
    event_price = models.FloatField()

    def event_already_happened(self):
        return evemt_end_date >= timezone.now()