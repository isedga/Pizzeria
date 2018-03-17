from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
import string

class RegistrationForm(UserCreationForm):
    username        = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter username'}), required=True)
    first_name      = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter first name'}), required=True)
    last_name       = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter last name'}), required=True)
    phone_number    = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter phone number'}), required=True)
    address         = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter address'}), required=True)
    address2        = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter address2'}), required=False)
    town            = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter town'}), required=True)
    zip_code        = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter zip code'}), required=True)
    state           = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter state'}), required=True)
    password1       = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter password'}), required=True)
    password2       = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter confirm password'}), required=True)
    
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'phone_number',
            'address',
            'address2',
            'town',
            'zip_code',
            'state',
            'password1',
            'password2'   
        )
        
# Allow to save the Data to the Model
def save(self, commit=True):
    user = super(RegistrationForm,self).save(commit=False)
    user.first_name      = self.cleaned_data['first_name']
    user.last_name       = self.cleaned_data['last_name']
    user.phone_number    = self.cleaned_data['phone_number']
    user.address         = self.cleaned_data['address']
    user.address2        = self.cleaned_data['address2']
    user.town            = self.cleaned_data['town']
    user.zip_code        = self.cleaned_data['zip_code']
    user.state           = self.cleaned_data['state']
    user.password1       = self.cleaned_data['password1']
    user.password2       = self.cleaned_data['password2']
    
    if commit:
        #User is going to be created in the database
        user.save()
        
    return user
        