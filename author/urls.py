from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('author', views.AuthorView)

urlpatterns = [
    # REST urls
    path('', include(router.urls)),
]