from django.db import models

# Create your models here.

app_name = 'pizzas'

class Pizza(models.Model):
    """Pizzas Types"""
    name = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)   

    def __str__(self):

        """Return a string representation of the model."""
        return "{0}".format(self.name) 
    
class Topping(models.Model):
    """Specific toppings for the pizza"""
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    name = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name_plural = 'toppings'
        def __str__(self):
            """Return a string representation of the model."""
            return self.name[:50] + "..."   
        
        