from django.contrib import admin

from .models import Pizza, Subs, Pasta, Salads, Dinner_Platters, Item
# Register your models here.

admin.site.register(Pizza)
admin.site.register(Subs)
admin.site.register(Pasta)
admin.site.register(Salads)
admin.site.register(Dinner_Platters)
admin.site.register(Item)