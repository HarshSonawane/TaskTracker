from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework import routers

from django.conf import settings
from django.conf.urls.static import static


router = routers.DefaultRouter()
router.register('tasks', views.TaskViewSet)
router.register('tasks-tracker', views.TaskTrackerViewSet)



urlpatterns = [
    path('', views.index),
    path('rest/', include(router.urls)),
]

urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)