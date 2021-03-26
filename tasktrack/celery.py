from __future__ import absolute_import, unicode_literals

import os

from celery import Celery
from celery.schedules import crontab

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tasktrack.settings')

app = Celery('tasktrack')
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.conf.beat_schedule = {
    'daily' : {
        'task' : 'task.tasks.every_day',
        'schedule' : crontab(minute=0, hour=17),
    },
    'weekly' : {
        'task' : 'task.tasks.every_monday_morning',
        'schedule' : crontab(hour=7, day_of_week='mon'),
    },
    'monthly' : {
        'task' : 'task.tasks.every_first_day',
        'schedule' : crontab(0, 0, day_of_month='1'),
    },
}


app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')


@app.task
def test(arg):
    print(arg)