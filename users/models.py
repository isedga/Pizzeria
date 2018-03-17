from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser
)
# Create your models here.

class User(models.Model):
    ''' Our User model. '''
    username         = models.CharField(max_length=25, null=True)
    first_name       = models.CharField(max_length=25, null=True)
    last_name        = models.CharField(max_length=25, null=True)
    phone_number     = models.CharField(max_length=10, null=True)
    address          = models.CharField(max_length=50, null=True)
    address2         = models.CharField(max_length=50, null=True) 
    town             = models.CharField(max_length=25, null=True)
    state            = models.CharField(max_length=2, null=True)
    zip_code         = models.CharField(max_length=5, null=True)
    password1        = models.CharField(max_length=25, null=True)
    password2        = models.CharField(max_length=25, null=True)

    def __str__(self):
        '''Return a string representation of the model.'''
        return  self.username
    
    
    
