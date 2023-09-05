from django.shortcuts import render, redirect
from .models import Snag
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.


def index(request):
    # Check to see if logged in
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        # Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Welcome to LCS Snags")
            return redirect("home")
        else:
            messages.success(request, "Error ,please try again")
            return redirect("home")
    else:
        return render(request, "snags/home.html", {})  # {"snags": Snag.objects.all()})


def logout_user(request):
    logout(request)
    messages.success(request, "You Logged Out succesfully")
    return redirect("home")


def register_user(request):
    return render(request, "register.html", {})
