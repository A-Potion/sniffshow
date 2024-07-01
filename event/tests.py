from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from .models import Event

import datetime

def make_event(enddays, startdays, event_name):
    starttime = timezone.now() + datetime.timedelta(days=startdays)
    endtime = timezone.now() + datetime.timedelta(days=enddays)
    return Event.objects.create(event_name=event_name, event_start_date=starttime, event_end_date = endtime, event_price=1)


class test_event_list(TestCase):
    def test_past_event(self):
        pastevent = make_event(enddays=-10, startdays=-11, event_name="Past event.")
        response = self.client.get(reverse("event:list"))
        return self.assertContains(response, "No events added for now! Check again soon!")
    
    def test_past_and_future_event(self):
        pastevent = make_event(enddays=-10, startdays=-11, event_name="Past event.")
        futureevent = make_event(enddays=12, startdays=11, event_name="Future event.")
        response = self.client.get(reverse("event:list"))
        return self.assertContains(response, futureevent.event_name)
    
    def test_future_event(self):
        futureevent = make_event(enddays=12, startdays=11, event_name="Past event.")
        response = self.client.get(reverse("event:list"))
        return self.assertContains(response, futureevent.event_name)
    