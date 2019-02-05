from django.http import HttpResponse
from django.shortcuts import render

from orders.forms import UserCreationForm
from django import forms
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


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
            return render(request, "index.html")
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

