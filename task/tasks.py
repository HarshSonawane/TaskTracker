from __future__ import absolute_import, unicode_literals
from celery import shared_task
from celery.task.schedules import crontab
from celery.decorators import periodic_task
from .models import TaskTracker


@shared_task
def every_monday_morning():
    tss = TaskTracker.objects.filter(task_type=2)
    for t in tss:
        print("Email sent to ", t.email)



@shared_task
def every_day():
    tss = TaskTracker.objects.filter(task_type=1)
    for t in tss:
        print("Email sent to ", t.email)



@shared_task
def every_first_day():
    tss = TaskTracker.objects.filter(task_type=3)
    for t in tss:
        print("Email sent to ", t.email)


@shared_task
def send_ee():
    print('Email Sent')
    return None