from django.db import models
from django import forms
"""from django.contrib.auth.models import (
    AbstractBaseUser
)"""
# Create your models here.

class Employees(models.Model):
    ''' Our Order model. '''
    
    PIZZA_SIZE = (
        ('30cm','30 CM'),
        ('40cm', '40 CM'),
        ('50cm','50 CM'),
        ('55cm','55 CM'),
    )  

    username       = models.CharField(max_length=25, null=True)
    address        = models.CharField(max_length=100, null=True)
    pizza = models.CharField('Pizzas', max_length=100,  null=True)
                                                 
    size           = models.CharField(max_length=6, choices=PIZZA_SIZE, default='30cm')

    def __str__(self):
        '''Return a string representation of the model.'''
        return  self.username
    
    
    
