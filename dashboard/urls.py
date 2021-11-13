from django import urls
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url

from .views import dashboard

urlpatterns = [
    url(r'^$', dashboard.as_view())  # You are already inside the dashboard resource
   
    
]

