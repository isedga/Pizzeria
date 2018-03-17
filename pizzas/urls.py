"""Defines URL patterns for pizzas."""
from django.conf.urls import url
from . import views

app_name = 'pizzas'
urlpatterns = [
    # Home page
    url(r'^$', views.index, name='index'),

    # Show all topics.
    url(r'^pizza/$', views.pizza, name='pizza'),
    
    # Detail page for a single topic
    url(r'^pizza/(?P<topping_id>\d+)/$', views.topping, name='topping'),  
       
]