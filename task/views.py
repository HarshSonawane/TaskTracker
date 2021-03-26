from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import generics
from . import serializers
from url_filter.integrations.drf import DjangoFilterBackend
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Task, TaskTracker
from django.http import HttpResponse
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from rest_framework.response import Response

from .tasks import send_ee, every_day


def index(request):
    every_day()
    return HttpResponse('Celery Done')


class TaskViewSet(viewsets.ModelViewSet):
    page_size = 50
    queryset = Task.objects.all().order_by('-created')
    serializer_class = serializers.TaskSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = '__all__'


class TaskTrackerViewSet(viewsets.ModelViewSet):
    page_size = 50
    queryset = TaskTracker.objects.all()
    serializer_class = serializers.TaskTrackerSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = '__all__'