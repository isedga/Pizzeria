from django.shortcuts import render
from .models import Pizza, Topping
from django.http import HttpResponseRedirect
from django.urls import reverse
import string
#from django.core.urlresolvers import reverse

from .models import Pizza


# Create your views here.
def index(request):
    """The home page for pizzas"""
    return render(request, 'pizzas/index.html')

def pizza(request):
    """Show all pizza."""
    pizza = Pizza.objects.order_by('date_added')
    context = {'pizza': pizza}
    return render(request, 'pizzas/pizza.html', context)

def topping(request, topping_id):
    #Show a sigle Pizza toppings
    topping = Pizza.objects.get(id=topping_id)
    entries = topping.topping_set.order_by('-date_added')
    context = {'topping': topping, 'entries': entries}
    return render(request, 'pizzas/topping.html', context) 


