from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.page_main, name='page_main'),
]
