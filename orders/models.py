from django.db import models
from django.conf import settings

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=64)
    size = models.CharField(max_length=64,blank=True)
    sort = models.CharField(max_length=64,blank=True)    
    price = models.FloatField( default=0, blank=True)

    def __str__(self):
        return f"{self.name}, {self.size}, {self.sort} - {self.price}$"

class OrderItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    topping_1 = models.CharField(max_length=64,blank=True)
    topping_2 = models.CharField(max_length=64,blank=True)
    topping_3 = models.CharField(max_length=64,blank=True)
    topping_4 = models.CharField(max_length=64,blank=True)
    extra_cheese = models.BooleanField(default=False)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.user}, {self.item.name}, {self.item.size}, {self.item.sort} ({self.topping_1},{self.topping_2},{self.topping_3},{self.topping_4})"

    def get_total_item_price(self):
        return self.quantity * self.item.price


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    ordered = models.BooleanField(default=False)
    payed = models.BooleanField(default=False)
    confirmed = models.BooleanField(default=False)
    being_delivered = models.BooleanField(default=False)

    def get_total(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_total_item_price()
        return total

    def __str__(self):
        return f"order#{self.id}, to {self.user}"
