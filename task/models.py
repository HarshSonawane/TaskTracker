from django.db import models


class Task(models.Model):
    T1 = 1
    T2 = 2
    T3 = 3
    TYPE_CHOICES = (
        (T1, 'Task Type 1'),
        (T2, 'Task Type 2'),
        (T3 , 'Task Type 3'),
    )

    
    task_type               = models.PositiveSmallIntegerField(choices=TYPE_CHOICES)
    task_desc               = models.CharField(max_length=1000)

    created              = models.DateTimeField(auto_now_add=True)
    updated              = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.task_desc



class TaskTracker(models.Model):
    U1 = 1
    U2 = 2
    U3 = 3
    UPDATE_CHOICES = (
        (U1, 'Daily'),
        (U2, 'Weekly'),
        (U3 , 'Monthly'),
    )
    T1 = 1
    T2 = 2
    T3 = 3
    TYPE_CHOICES = (
        (T1, 'Task Type 1'),
        (T2, 'Task Type 2'),
        (T3 , 'Task Type 3'),
    )
    
    task_type       = models.PositiveSmallIntegerField(choices=TYPE_CHOICES)
    update_type     = models.PositiveSmallIntegerField(choices=UPDATE_CHOICES)
    email           = models.EmailField(unique=True)


    def __str__(self):
        return str(self.task_type) + str(self.update_type)
    