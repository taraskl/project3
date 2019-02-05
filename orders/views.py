from django.http import HttpResponse
from django.shortcuts import render

from django import forms
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from orders.forms import UserCreationForm
from orders.models import Pizza, Subs, Pasta, Salads, Dinner_Platters

# Create your views here.
def index(request):
    # user = authenticate(username='john', password='secret')
    # if user is not None:
    #     pass
    # else:
    #     pass
    # context = {
    #     "users": User.objects.all()
    # }
    return render(request, "index.html")

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            context = {
                "pizza": Pizza.objects.all(),
                "subs": Subs.objects.all(),
                "pasta": Pasta.objects.all(),
                "salads": Salads.objects.all(),
                "dinner_platters": Dinner_Platters.objects.all(),
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
        "pizza": Pizza.objects.all(),
        "subs": Subs.objects.all(),
        "pasta": Pasta.objects.all(),
        "salads": Salads.objects.all(),
        "dinner_platters": Dinner_Platters.objects.all(),
    }
    if request.method == "POST":
        try:
            regular_pizza_small = request.POST['regular_pizza_small']
            regular_pizza_large = request.POST['regular_pizza_large']
        except:
            pass    
        topping_1 = request.POST['topping_1']
        print(regular_pizza_small)

        return render(request, "menu.html", context)

    return render(request, "menu.html", context) 

