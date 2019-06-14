from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=64)
    size = models.CharField(max_length=64,blank=True)
    sort = models.CharField(max_length=64,blank=True)    
    topping_1 = models.CharField(max_length=64,blank=True)
    topping_2 = models.CharField(max_length=64,blank=True)
    topping_3 = models.CharField(max_length=64,blank=True)
    topping_4 = models.CharField(max_length=64,blank=True)
    extra_cheese = models.BooleanField(default=False)
    price = models.FloatField( default=0, blank=True)

    def __str__(self):
        return f"{self.name}, {self.size}, {self.sort} - {self.price}$"



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
    steak_adds = models.CharField(max_length=64,choices=STEAK_ADDS, blank=True)
    extra_cheese = models.BooleanField(default=False)
    price = models.FloatField(default=0, blank=True)

    def save(self, *args, **kwargs):
        # calculate price for Subs  
        if self.sort in ('Cheese' , 'Italian' , 'Ham + Cheese' , 'Meatball' , 'Tuna' , 'Eggplant Parmigiana'):
            self.price = 6.50
            if self.size == 'Large':
                self.price = 7.95
        elif self.sort in ('Turkey' , 'Chicken Parmigiana'):
            self.price = 7.50
            if self.size == 'Large':
                self.price = 8.50
        elif self.sort == 'Sausage, Peppers & Onions':
            self.price = 8.50 
        elif self.sort == 'Hamburger':
            self.price = 4.60
            if self.size == 'Large':
                self.price = 6.95
        elif self.sort == 'Cheeseburger':
            self.price = 5.10
            if self.size == 'Large':
                self.price = 7.45
        elif self.sort in ('Fried Chicken' , 'Veggie'):
            self.price = 6.95
            if self.size == 'Large':
                self.price = 8.50
        elif self.sort == 'Steak':
            self.price = 6.50
            if self.size == 'Large':
                self.price = 7.95
        elif self.sort == 'Steak + Cheese':
            self.price = 6.95
            if self.size == 'Large':
                self.price = 8.50

        super().save(*args, **kwargs)

        if self.sort in ('Steak' , 'Steak + Cheese'):
            if self.steak_adds in ('Mushrooms' , 'Green Peppers' , 'Onions'):
                self.price += 0.5  

        super().save(*args, **kwargs) 

        if self.extra_cheese == True:
            self.price += 0.50   

        super().save(*args, **kwargs) 

    def __str__(self):
        return f"{self.sort} ({self.size}) {self.price}$"

class Pasta(models.Model):    
    PASTA_SORT = (
        ('Baked Ziti w/Mozzarella','Baked Ziti w/Mozzarella'),
        ('Baked Ziti w/Meatballs','Baked Ziti w/Meatballs'),
        ('Baked Ziti w/Chicken','Baked Ziti w/Chicken'),
    )
    sort = models.CharField(max_length=64,choices=PASTA_SORT)
    price = models.FloatField(default=0, blank=True)

    def save(self, *args, **kwargs):
        # calculate price for Subs  
        if self.sort == 'Baked Ziti w/Mozzarella':
            self.price = 6.50
        elif self.sort == 'Baked Ziti w/Meatballs':
            self.price = 8.75
        elif self.sort == 'Baked Ziti w/Chicken':
            self.price = 9.75
        super().save(*args, **kwargs) 

    def __str__(self):
        return f"{self.sort} {self.price}$"

class Salads (models.Model):    
    SALADS_SORT = (
        ('Garden Salad','Garden Salad'),
        ('Greek Salad','Greek Salad'),
        ('Antipasto','Antipasto'),
        ('Salad w/Tuna','Salad w/Tuna'),
    )
    sort = models.CharField(max_length=64,choices=SALADS_SORT)
    price = models.FloatField(default=0, blank=True)

    def save(self, *args, **kwargs):
        # calculate price for Subs  
        if self.sort == 'Garden Salad':
            self.price = 6.25
        elif self.sort in ('Greek Salad', 'Antipasto', 'Salad w/Tuna'):
            self.price = 8.25
        super().save(*args, **kwargs) 

    def __str__(self):
        return f"{self.sort} {self.price}$"

class Dinner_Platters (models.Model):    
    DINNER_SORT = (
        ('Garden Salad','Garden Salad'),
        ('Greek Salad','Greek Salad'),
        ('Antipasto','Antipasto'),
        ('Baked Ziti','Baked Ziti'),
        ('Meatball Parm','Meatball Parm'),
        ('Chicken Parm','Chicken Parm'),
    )
    DINNER_SIZE = (
        ('Small','Small'),
        ('Large','Large'),
    )
    sort = models.CharField(max_length=64,choices=DINNER_SORT)
    size = models.CharField(max_length=64,choices=DINNER_SIZE)
    price = models.FloatField(default=0, blank=True)

    def save(self, *args, **kwargs):
        # calculate price for Subs  
        if self.sort == 'Garden Salad':
            self.price = 35.0
            if self.size == 'Large':
                self.price = 60.0
        elif self.sort in ('Greek Salad', 'Antipasto', 'Meatball Parm'):
            self.price = 45.0
            if self.size == 'Large':
                self.price = 70.0 
        elif self.sort == 'Baked Ziti':
            self.price = 35.0
            if self.size == 'Large':
                self.price = 70.0 
        elif self.sort == 'Chicken Parm':
            self.price = 45.0
            if self.size == 'Large':
                self.price = 80.0 
        super().save(*args, **kwargs) 

    def __str__(self):
        return f"{self.sort} ({self.size}) {self.price}$"
''' To do models:

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