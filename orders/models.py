from django.db import models

# Create your models here.
class Pizza(models.Model):
    PIZZA_SORT = (
        ('Regular Pizza','Regular Pizza'),
        ('Sicilian Pizza','Sicilian Pizza'),
    )
    PIZZA_SIZE = (
        ('Small','Small'),
        ('Large','Large'),
    )
    PIZZA_TOPPINGS = (
        ('Pepperoni','Pepperoni'),
        ('Sausage','Sausage'),
        ('Mushrooms','Mushrooms'),
        ('Onions','Onions'),
        ('Ham','Ham'),
        ('Canadian Bacon','Canadian Bacon'),
        ('Pineapple','Pineapple'),
        ('Eggplant','Eggplant'),
        ('Tomato & Basil','Tomato & Basil'),
        ('Green Peppers','Green Peppers'),
        ('Hamburger','Hamburger'),
        ('Spinach','Spinach'),
        ('Artichoke','Artichoke'),
        ('Buffalo Chicke','Buffalo Chicke'),
        ('Barbecue Chicken','Barbecue Chicken'),
        ('Anchovies','Anchovies'),
        ('Black Olives','Black Olives'),
        ('Fresh Garlic','Fresh Garlic'),
        ('Zucchini','Zucchini'),
    )
    sort = models.CharField(max_length=64,choices=PIZZA_SORT)
    size = models.CharField(max_length=64,choices=PIZZA_SIZE)
    topping_1 = models.CharField(max_length=64,choices=PIZZA_TOPPINGS, blank=True)
    topping_2 = models.CharField(max_length=64,choices=PIZZA_TOPPINGS, blank=True)
    topping_3 = models.CharField(max_length=64,choices=PIZZA_TOPPINGS, blank=True)
    topping_4 = models.CharField(max_length=64,choices=PIZZA_TOPPINGS, blank=True)
    price = models.FloatField( default=0, blank=True)

    def save(self, *args, **kwargs):
        # calculate price for Regular Pizza  
        if self.sort == 'Regular Pizza' and self.size == 'Small' and self.topping_1 == '' and self.topping_2 == '' and self.topping_3 == '' and self.topping_4 == '':
            self.price = 12.20
        elif self.sort == 'Regular Pizza' and self.size == 'Small' and self.topping_1 != '' and self.topping_2 == '' and self.topping_3 == '' and self.topping_4 == '':
            self.price = 13.20
        elif self.sort == 'Regular Pizza' and self.size == 'Small' and self.topping_1 != '' and self.topping_2 != '' and self.topping_3 == '' and self.topping_4 == '':
            self.price = 14.70
        elif self.sort == 'Regular Pizza' and self.size == 'Small' and self.topping_1 != '' and self.topping_2 != '' and self.topping_3 != '' and self.topping_4 == '':
            self.price = 15.70
        elif self.sort == 'Regular Pizza' and self.size == 'Small' and self.topping_1 != '' and self.topping_2 != '' and self.topping_3 != '' and self.topping_4 != '':
            self.price = 17.25 
        elif self.sort == 'Regular Pizza' and self.size == 'Large' and self.topping_1 == '' and self.topping_2 == '' and self.topping_3 == '' and self.topping_4 == '':
            self.price = 17.45
        elif self.sort == 'Regular Pizza' and self.size == 'Large' and self.topping_1 != '' and self.topping_2 == '' and self.topping_3 == '' and self.topping_4 == '':
            self.price = 19.45
        elif self.sort == 'Regular Pizza' and self.size == 'Large' and self.topping_1 != '' and self.topping_2 != '' and self.topping_3 == '' and self.topping_4 == '':
            self.price = 21.45
        elif self.sort == 'Regular Pizza' and self.size == 'Large' and self.topping_1 != '' and self.topping_2 != '' and self.topping_3 != '' and self.topping_4 == '':
            self.price = 23.45
        elif self.sort == 'Regular Pizza' and self.size == 'Large' and self.topping_1 != '' and self.topping_2 != '' and self.topping_3 != '' and self.topping_4 != '':
            self.price = 25.45
        # calculate price for Sicilian Pizza  
        elif self.sort == 'Sicilian Pizza' and self.size == 'Small' and self.topping_1 == '' and self.topping_2 == '' and self.topping_3 == '' and self.topping_4 == '':
            self.price = 23.45
        elif self.sort == 'Sicilian Pizza' and self.size == 'Small' and self.topping_1 != '' and self.topping_2 == '' and self.topping_3 == '' and self.topping_4 == '':
            self.price = 25.45
        elif self.sort == 'Sicilian Pizza' and self.size == 'Small' and self.topping_1 != '' and self.topping_2 != '' and self.topping_3 == '' and self.topping_4 == '':
            self.price = 27.45
        elif self.sort == 'Sicilian Pizza' and self.size == 'Small' and self.topping_1 != '' and self.topping_2 != '' and self.topping_3 != '' and self.topping_4 == '':
            self.price = 28.45
        elif self.sort == 'Sicilian Pizza' and self.size == 'Small' and self.topping_1 != '' and self.topping_2 != '' and self.topping_3 != '' and self.topping_4 != '':
            self.price = 29.45
        elif self.sort == 'Sicilian Pizza' and self.size == 'Large' and self.topping_1 == '' and self.topping_2 == '' and self.topping_3 == '' and self.topping_4 == '':
            self.price = 37.70
        elif self.sort == 'Sicilian Pizza' and self.size == 'Large' and self.topping_1 != '' and self.topping_2 == '' and self.topping_3 == '' and self.topping_4 == '':
            self.price = 39.70
        elif self.sort == 'Sicilian Pizza' and self.size == 'Large' and self.topping_1 != '' and self.topping_2 != '' and self.topping_3 == '' and self.topping_4 == '':
            self.price = 41.70
        elif self.sort == 'Sicilian Pizza' and self.size == 'Large' and self.topping_1 != '' and self.topping_2 != '' and self.topping_3 != '' and self.topping_4 == '':
            self.price = 43.70
        elif self.sort == 'Sicilian Pizza' and self.size == 'Large' and self.topping_1 != '' and self.topping_2 != '' and self.topping_3 != '' and self.topping_4 != '':
            self.price = 44.70  
        else:
            pass
        super().save(*args, **kwargs) 

    def __str__(self):
        return f"{self.sort} ({self.size}) {self.price}$"

class Subs(models.Model):
    SUBS_SORT = (
        ('Cheese','Cheese'),
        ('Italian','Italian'),
        ('Ham + Cheese','Ham + Cheese'),
        ('Meatball','Meatball'),
        ('Tuna','Tuna'),
        ('Turkey','Turkey'),
        ('Chicken Parmigiana','Chicken Parmigiana'),
        ('Eggplant Parmigiana','Eggplant Parmigiana'),
        ('Steak','Steak'),
        ('Steak + Cheese','Steak + Cheese'),
        ('Sausage, Peppers & Onions','Sausage, Peppers & Onions'),
        ('Hamburger','Hamburger'),
        ('Cheeseburger','Cheeseburger'),
        ('Fried Chicken','Fried Chicken'),
        ('Veggie','Veggie'),
    )
    SUBS_SIZE = (
        ('Small','Small'),
        ('Large','Large'),
    )
    STEAK_ADDS = (
        ('Mushrooms','Mushrooms'),
        ('Green Peppers','Green Peppers'),
        ('Onions','Onions'),
    )
    sort = models.CharField(max_length=64,choices=SUBS_SORT)
    size = models.CharField(max_length=64,choices=SUBS_SIZE)
    steak_adds = models.CharField(max_length=64,choices=STEAK_ADDS)
    extra_cheese = models.BooleanField(default=False)
    price = models.FloatField(default=0, blank=True)

    def __str__(self):
        return f"{self.sort} ({self.size}) {self.price}$"

''' To do models:
Subs
    sort
    steak_adds
    extra_cheese
    price

Pasta
    sort
    price

Salads      
    sort
    price

Dinner Platters
    sort
    size    
    price
''' 