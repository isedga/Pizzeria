from django import forms
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login, logout, authenticate
from users.forms import RegistrationForm
import string

# Create your views here.

def logout_view(request):
 """Log the user out."""
 logout(request)
 return HttpResponseRedirect(reverse('pizzas:index'))

# registration function
  
def register(request):
# Register a new user.
 if request.method != 'POST': 
  # Display blank registration form.
  form = RegistrationForm()
 else:
     # Process completed form.
     form = RegistrationForm(data=request.POST)
     if form.is_valid():
      new_user = form.save()
      return redirect('/pizza')
 context = {'form': form}
 return render(request, 'users/register.html', context)     

