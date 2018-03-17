from django import forms
from django.shortcuts import render,redirect
from django.urls import reverse
from orders.forms import OrderForm
import string

# Create your views here.

# orders function

def orders(request):
# Register a new user.
    if request.method != 'POST': 
        # Display blank registration form.
        form = OrderForm()
    else:
        # Process completed form.
        form = OrderForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            return redirect('/pizza')
    context = {'form': form}
    return render(request, 'orders/ordering.html', context)     

