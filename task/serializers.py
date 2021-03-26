from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Task, TaskTracker


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ['id', 'task_type', 'task_desc']


class TaskTrackerSerializer(serializers.ModelSerializer):

    class Meta:
        model = TaskTracker
        fields = ['id', 'task_type', 'update_type', 'email']
