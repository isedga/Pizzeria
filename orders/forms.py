from django import forms
from .models import Employees
import string

PIZZA_TYPE = (
    ('Sicilian', 'SICILIAN'),
    ('Neapolitan', 'NEAPOLITAN'),
    ('Hawaiian', 'HAWAIIAN'),
    ('MeatLovers', 'MEATLOVERS'),
    ('Margherita', 'MARGHERITA')
     
)

class OrderForm(forms.ModelForm):
    username      = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter customer name'}), required=True)
    address         = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter customer address'}), required=True)
    pizza = forms.ChoiceField(label='Customer favorite pizza',choices=PIZZA_TYPE,widget=forms.RadioSelect())                                 

    class Meta:
        model = Employees
        fields = (
            'username',
            'address',
            'pizza',
            'size'  
        )
        
# Allow to save the Data to the Model
def save(self, commit=True):
    customer = super(OrderForm,self).save(commit=True)
    customer.username      = self.cleaned_data['username ']
    customer.address         = self.cleaned_data['address']
    customer.pizza         = self.cleaned_data['pizza']    
    customer.size            = self.cleaned_data['size']
   
    if commit:
        #Employees is going to be created in the database
        customer.save()  
    return customer
