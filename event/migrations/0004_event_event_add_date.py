# Generated by Django 5.0.6 on 2024-07-02 18:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0003_alter_event_event_end_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='event_add_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 2, 18, 23, 23, 37860, tzinfo=datetime.timezone.utc), verbose_name='event add date'),
            preserve_default=False,
        ),
    ]
