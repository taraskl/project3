from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone

from django import forms
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from orders.forms import UserCreationForm
from orders.models import Item, Order, OrderItem

# Create your views here.
def index(request):
    return render(request, "index.html")

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            context = {
                "items": Item.objects.all(),
                "username": username,
            }
            return render(request, "menu.html", context)
        else:
            # To do: Return an 'invalid login' error message.
            return render(request, "index.html")   

    return render(request, "login.html")

def logout_view(request):
    logout(request)
    return render(request, "index.html")   

def signup_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "index.html") 
    else:        
        form = UserCreationForm()

    return render(request, "signup.html", { "form":form }) 


def menu_view(request):
    context = {
        "items": Item.objects.all(),
        "username": request.user,
    }
    if request.method == "POST":
        item_id = request.POST['id']
        item = Item.objects.get(id=item_id)
        order_item, created = OrderItem.objects.get_or_create(
            item=item,
            user=request.user,
            ordered=False
        )
        #add toppings to order item
        if item.sort in ['1 topping', '2 toppings', '3 toppings', 'Special']:
            topping_1 = request.POST['topping_1']
            order_item.topping_1 = topping_1
            order_item.save()
        if item.sort in ['2 toppings', '3 toppings', 'Special']:
            topping_2 = request.POST['topping_2']
            order_item.topping_2 = topping_2
            order_item.save()
        if item.sort in ['3 toppings', 'Special']:
            topping_3 = request.POST['topping_3']
            order_item.topping_3 = topping_3
            order_item.save()    
        if item.sort in ['Special']:
            topping_4 = request.POST['topping_4']
            order_item.topping_4 = topping_4
            order_item.save()  

        order_qs = Order.objects.filter(user=request.user, ordered=False)
        if order_qs.exists():
            order = order_qs[0]
            order.items.add(order_item)
            order.save()
        else:
            order = Order.objects.create(
                user=request.user)
            order.items.add(order_item)
            order.save()
        return render(request, "menu.html", context)

    return render(request, "menu.html", context) 

def cart_view(request):
    try:
        order = Order.objects.get(user=request.user, ordered=False)
        context = {
            'object': order,
            "username": request.user,
        }
        return render(request, 'cart.html', context)
    except:
        context = {
            "username": request.user,
        }
        return render(request, "cart.html",context)

def success_view(request):
    order_id = request.POST['order_id']
    order = Order.objects.get(id=order_id)
    order.ordered = True
    order.save()
    return render(request, "success.html")       

def orders_view(request):
    try:
        orders = Order.objects.filter(user=request.user, ordered=True)
        context = {
            'orders': orders,
            "username": request.user,
        }
        print(type(orders))
        return render(request, 'orders.html', context)
    except:
        context = {
            "username": request.user,
        }
        print("Noooo")
        return render(request, "orders.html",context)