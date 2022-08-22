from __future__ import absolute_import, unicode_literals 
import os

from celery import Celery
from celery.schedules import crontab

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sendjoke.settings')

app = Celery('sendjoke')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.update(timezone= 'Africa/Nairobi')

app.conf.beat_schedule = {
    "send-mail-after- 10- min":{
        'task': 'joke.tasks.send_mail_func',
        'schedule': crontab(minute=0, hour=0)
    }

}

# Load task modules from all registered Django apps.
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')