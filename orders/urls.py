"""Defines URL patterns for users"""
from django.conf.urls import url
from . import views

app_name = 'orders'

urlpatterns = [
# Order page
url(r'^orders/$', views.orders, name='orders'),
]